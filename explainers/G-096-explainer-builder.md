# One file between a finding and a dependable page

The explainer builder is now a standalone, standard-library script. A project declares Markdown pages, navigation, assets, output and explainer metadata in JSON; the script writes committed HTML and `--check` proves that rebuilding produces the same bytes.

## 1. What was built

The old ADUS renderer knew three filenames, three titles and one stylesheet in Python. Those choices now live in `site/site.json`. The script itself can take any config:

```sh
python3 site/build.py --config path/to/site.json
python3 site/build.py --config path/to/site.json --check
```

<svg viewBox="0 0 760 180" role="img" aria-label="A JSON config and Markdown sources enter one standard-library builder, which emits committed HTML and declared assets before validation loops back over the output">
  <defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent, #704b8b)"/></marker></defs>
  <rect x="10" y="42" width="170" height="88" rx="12" fill="var(--notice-bg, #f2eadc)" stroke="var(--line, #ded6c8)"/>
  <text x="95" y="76" text-anchor="middle" fill="var(--ink, #23211d)" font-weight="700">JSON config</text>
  <text x="95" y="101" text-anchor="middle" fill="var(--muted, #6f6a60)">Markdown + assets</text>
  <path d="M 190 86 H 278" stroke="var(--accent, #704b8b)" stroke-width="3" marker-end="url(#arrow)"/>
  <rect x="290" y="42" width="180" height="88" rx="12" fill="var(--accent-soft, #e5efe9)" stroke="var(--accent, #704b8b)"/>
  <text x="380" y="76" text-anchor="middle" fill="var(--ink, #23211d)" font-weight="700">build.py</text>
  <text x="380" y="101" text-anchor="middle" fill="var(--muted, #6f6a60)">standard library only</text>
  <path d="M 482 86 H 570" stroke="var(--accent, #704b8b)" stroke-width="3" marker-end="url(#arrow)"/>
  <rect x="582" y="42" width="168" height="88" rx="12" fill="var(--notice-bg, #f2eadc)" stroke="var(--line, #ded6c8)"/>
  <text x="666" y="76" text-anchor="middle" fill="var(--ink, #23211d)" font-weight="700">Committed output</text>
  <text x="666" y="101" text-anchor="middle" fill="var(--muted, #6f6a60)">HTML + assets</text>
  <path d="M 666 142 V 164 H 380 V 142" fill="none" stroke="var(--accent, #704b8b)" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arrow)"/>
  <text x="520" y="176" text-anchor="middle" fill="var(--muted, #6f6a60)" font-size="12">--check: routes · metadata · exact bytes</text>
</svg>

## 2. What was observed

The migration changed none of the three existing ADUS pages: a clean rebuild is byte-identical to the committed `index.html`, `report.html`, `glossary.html`, their styles and every section anchor.

The exact fixture that selected this substrate now passes where the old builder failed. Its `second.md` link becomes `second.html`, its separate SVG is copied only because the config declares it, and its inline SVG remains an SVG element. Five tests also prove that incomplete metadata and SVG carrying scripts, event handlers, embedded styles, foreign objects or external fetches are rejected.

This page is the real close-out trial. It was authored in Markdown, its declaration block came from config, the diagram above went through the audited SVG path, and the HTML you are reading is committed output.

## 3. What that could mean

The strongest reading is narrow: this is enough common substrate for dated explainers without making a documentation framework own every project. Repositories with a working hand-authored or generated site keep it. Repositories without one can adopt a single script and config, while the renderer-independent `EXPLAINERS.md` convention continues to own what a page must declare.

A broader reading — that this should become the portfolio's general static-site generator — is not supported. The Markdown subset is deliberately small; there is no search, plugin system or theme package. MkDocs remains the escalation path if shared navigation or search becomes the real requirement.

## 4. What could be used or tested next

A future goal that owes a digest can either use its project's existing substrate or point this builder at a small project-owned config. The useful next test is adoption in a second repository, because that will expose which shell fields are genuinely general and which only looked general while ADUS was the sole permanent user.

## Implementation detail

The source-to-output map drives `.md` route rewriting. Asset sources and destinations are explicit, including directories. Inline SVG is parsed as XML and accepted only as one complete block with a `viewBox` and accessible name. Validation follows every generated `href` and `src`, checks fragments, confirms configured explainer metadata is visible, and compares a temporary build with committed output under `--check`.

The weakest point is the parser boundary: it intentionally supports the Markdown this portfolio's explainers currently use, not CommonMark in full. Nested lists, arbitrary HTML and extension syntax should trigger a decision to improve the subset or use MkDocs, not an accumulation of ad hoc exceptions.
