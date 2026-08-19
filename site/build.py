#!/usr/bin/env python3
"""Build the dependency-free ADUS static site."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "index.html": ROOT / "README.md",
    "report.html": ROOT / "ADUS-tech-report-v1.4.md",
    "glossary.html": ROOT / "ADUS-glossary-v1.4.md",
}
TITLES = {
    "index.html": "ADUS — a functional architecture of intelligence",
    "report.html": "ADUS Framework — Technical Report v1.4",
    "glossary.html": "ADUS v1.4 — Glossary",
}


def plain(text: str) -> str:
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"[*_`]+", "", text).strip()


def slug(text: str) -> str:
    value = plain(text).lower().replace("§", "section-")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "section"


def section_number(text: str) -> str | None:
    match = re.match(r"(\d+(?:\.\d+)*)\b", plain(text))
    return match.group(1) if match else None


def heading_data(source: Path) -> tuple[dict[str, str], list[tuple[int, str, str]]]:
    sections: dict[str, str] = {}
    headings: list[tuple[int, str, str]] = []
    used: dict[str, int] = {}
    for line in source.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        level, text = len(match.group(1)), plain(match.group(2))
        base = slug(text)
        count = used.get(base, 0)
        used[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count + 1}"
        headings.append((level, text, anchor))
        number = section_number(text)
        if number:
            sections[number] = anchor
    return sections, headings


REPORT_SECTIONS, _ = heading_data(SOURCES["report.html"])


def link_target(target: str) -> str:
    if target in {"docs/", "docs"}:
        return "index.html"
    if target.endswith("ADUS-tech-report-v1.4.md"):
        return "report.html"
    if target.endswith("ADUS-glossary-v1.4.md"):
        return "glossary.html"
    return target


def inline(text: str, page: str) -> str:
    tokens: list[str] = []

    def hold(value: str) -> str:
        tokens.append(value)
        return f"\x00{len(tokens) - 1}\x00"

    def markdown_link(match: re.Match[str]) -> str:
        label, target = match.group(1), link_target(match.group(2))
        return hold(f'<a href="{html.escape(target, quote=True)}">{html.escape(label)}</a>')

    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)", markdown_link, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", lambda m: hold(f"<code>{m.group(1)}</code>"), text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    report_prefix = "" if page == "report.html" else "report.html"

    def section_link(match: re.Match[str]) -> str:
        number = match.group(1)
        anchor = REPORT_SECTIONS.get(number)
        if not anchor:
            return match.group(0)
        return f'<a class="section-ref" href="{report_prefix}#{anchor}">§{number}</a>'

    text = re.sub(r"§(\d+(?:\.\d+)*)", section_link, text)
    text = re.sub(
        r"(?<![\"'=])(https?://[^\s<]+)",
        lambda m: f'<a href="{m.group(1).rstrip(".,;")}">{m.group(1).rstrip(".,;")}</a>{m.group(1)[len(m.group(1).rstrip(".,;")):]}' ,
        text,
    )
    for index, value in enumerate(tokens):
        text = text.replace(f"\x00{index}\x00", value)
    return text


def render_markdown(source: Path, page: str) -> tuple[str, list[tuple[int, str, str]]]:
    lines = source.read_text(encoding="utf-8").splitlines()
    _, headings = heading_data(source)
    heading_iter = iter(headings)
    output: list[str] = []
    paragraph: list[str] = []
    list_kind: str | None = None
    in_code = False
    code_lines: list[str] = []
    i = 0

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline(' '.join(part.strip() for part in paragraph), page)}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            output.append(f"</{list_kind}>")
            list_kind = None

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush_paragraph(); close_list()
            if in_code:
                output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines.clear()
            in_code = not in_code
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        if i + 1 < len(lines) and line.startswith("|") and re.match(r"^\|?\s*:?-+", lines[i + 1]):
            flush_paragraph(); close_list()
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            output.append('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{inline(c, page)}</th>" for c in rows[0]) + "</tr></thead><tbody>")
            for row in rows[2:]:
                output.append("<tr>" + "".join(f"<td>{inline(c, page)}</td>" for c in row) + "</tr>")
            output.append("</tbody></table></div>")
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            flush_paragraph(); close_list()
            level, text, anchor = next(heading_iter)
            output.append(f'<h{level} id="{anchor}">{inline(text, page)}<a class="permalink" href="#{anchor}" aria-label="Link to this section">#</a></h{level}>')
            i += 1
            continue
        item = re.match(r"^\s*([*-]|\d+\.)\s+(.+)$", line)
        if item:
            flush_paragraph()
            kind = "ol" if item.group(1)[0].isdigit() else "ul"
            if list_kind != kind:
                close_list(); output.append(f"<{kind}>"); list_kind = kind
            item_parts = [item.group(2)]
            i += 1
            while i < len(lines) and lines[i].strip():
                continuation = lines[i]
                if (re.match(r"^\s*([*-]|\d+\.)\s+", continuation)
                        or re.match(r"^#{1,6}\s+", continuation)
                        or re.match(r"^\s*---+\s*$", continuation)
                        or continuation.startswith(("```", "> ", "|"))):
                    break
                item_parts.append(continuation.strip())
                i += 1
            output.append(f"<li>{inline(' '.join(item_parts), page)}</li>")
            continue
        if re.match(r"^\s*---+\s*$", line):
            flush_paragraph(); close_list(); output.append("<hr>"); i += 1; continue
        if line.startswith("> "):
            flush_paragraph(); close_list(); output.append(f"<blockquote>{inline(line[2:], page)}</blockquote>"); i += 1; continue
        if not line.strip():
            flush_paragraph(); close_list(); i += 1; continue
        paragraph.append(line)
        i += 1
    flush_paragraph(); close_list()
    if in_code:
        raise ValueError(f"Unclosed code fence in {source}")
    return "\n".join(output), headings


def toc(headings: list[tuple[int, str, str]]) -> str:
    items = [f'<li class="toc-level-{level}"><a href="#{anchor}">{html.escape(text)}</a></li>' for level, text, anchor in headings if 2 <= level <= 3]
    return '<nav class="toc" aria-label="On this page"><h2>On this page</h2><ol>' + "".join(items) + "</ol></nav>" if items else ""


def shell(page: str, body: str, headings: list[tuple[int, str, str]]) -> str:
    nav = "".join(f'<a href="{href}"{(" aria-current=\"page\"" if href == page else "")}>{label}</a>' for href, label in (("index.html", "Overview"), ("report.html", "Technical report"), ("glossary.html", "Glossary")))
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="ADUS v1.4 framework documents">
  <title>{html.escape(TITLES[page])}</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#content">Skip to content</a>
  <header class="site-header"><a class="brand" href="index.html">ADUS <span>v1.4</span></a><nav aria-label="Primary">{nav}</nav></header>
  <div class="layout">{toc(headings)}<main id="content">{body}</main></div>
  <footer><p>Independent research · <a href="https://github.com/symbolfarm/retention-bench">Retention Bench</a> measures the consolidation claims.</p></footer>
</body>
</html>
'''


def build(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for page, source in SOURCES.items():
        body, headings = render_markdown(source, page)
        (destination / page).write_text(shell(page, body, headings), encoding="utf-8", newline="\n")
    shutil.copyfile(ROOT / "site" / "styles.css", destination / "styles.css")
    (destination / ".nojekyll").write_text("", encoding="utf-8")
    validate(destination)


def validate(destination: Path) -> None:
    pages = {path.name: path.read_text(encoding="utf-8") for path in destination.glob("*.html")}
    ids = {name: set(re.findall(r'\bid="([^"]+)"', text)) for name, text in pages.items()}
    errors: list[str] = []
    for name, text in pages.items():
        if 'name="viewport"' not in text:
            errors.append(f"{name}: missing viewport")
        for href in re.findall(r'href="([^"]+)"', text):
            parsed = urlsplit(href)
            if parsed.scheme or href.startswith("mailto:"):
                continue
            target_name = parsed.path or name
            target = destination / target_name
            if not target.exists():
                errors.append(f"{name}: missing target {href}")
            elif parsed.fragment and parsed.fragment not in ids.get(target_name, set()):
                errors.append(f"{name}: missing fragment {href}")
    if errors:
        raise SystemExit("Link validation failed:\n" + "\n".join(errors))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if committed build is stale")
    args = parser.parse_args()
    destination = ROOT / "docs"
    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp)
            build(candidate)
            expected = {p.relative_to(candidate): p.read_bytes() for p in candidate.rglob("*") if p.is_file()}
            actual = {p.relative_to(destination): p.read_bytes() for p in destination.rglob("*") if p.is_file()} if destination.exists() else {}
            if expected != actual:
                missing = sorted(str(p) for p in expected.keys() - actual.keys())
                extra = sorted(str(p) for p in actual.keys() - expected.keys())
                changed = sorted(str(p) for p in expected.keys() & actual.keys() if expected[p] != actual[p])
                raise SystemExit(f"docs/ is stale (missing={missing}, extra={extra}, changed={changed})")
            print("docs/ is reproducible and all local links resolve")
    else:
        build(destination)
        print(f"Built {len(SOURCES)} pages in {destination}")


if __name__ == "__main__":
    main()
