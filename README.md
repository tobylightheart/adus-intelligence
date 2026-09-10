# ADUS — a functional architecture of intelligence

**ADUS** describes intelligence as four continuously interacting components:
**abilities**, **dispositions**, **understandings** and **skills**. It is a
*functional* architecture — components are identified by role and information
flow rather than by substrate — which is what lets the same vocabulary apply to
human and artificial systems, and what makes it usable for both pedagogy and
AI design.

This repository is the home of the framework documents.

## Contents

| Document | What it is |
| --- | --- |
| [ADUS-tech-report-v1.4.md](ADUS-tech-report-v1.4.md) | The framework itself: component model, zones, consolidation channels, automaticity / awareness / controllability parameters, proposed assays, and nine falsifiable claims. |
| [ADUS-glossary-v1.4.md](ADUS-glossary-v1.4.md) | Term-by-term reference, with notation and the distinctions the framework depends on. Read alongside the report rather than after it. |
| [Builder close-out](docs/explainer-builder-2026-09-10.html) | A dated, not-human-reviewed digest of the standalone explainer builder: what changed, what the fixture proved, and where its deliberately small Markdown boundary sits. |

Both framework documents are v1.4 (2026-07-29). The report opens with a changelog against v1.3.

## Read online

The committed static build lives in [`docs/`](docs/) and is ready for GitHub
Pages to serve from the `main` branch's `/docs` directory.

## Build the site

The build has no package or network dependencies; Python 3's standard library
is enough. Site-specific pages, navigation, assets and output live in
[`site/site.json`](site/site.json); the builder itself has no ADUS-specific
source or title map.

```sh
python3 site/build.py
python3 site/build.py --check
```

The first command regenerates `docs/`. The second builds into a temporary
directory, checks every local page, section link, declared asset and explainer
metadata field, and verifies that the result is byte-for-byte identical to the
committed build. CI runs the check on every push and pull request.

The script is also a standalone explainer builder. Pass another JSON file with
`--config path/to/site.json`; relative source, asset and output paths resolve
from that config's directory. A config declares:

- `pages`: Markdown source → HTML output and title, with an optional `explainer`
  declaration (`layer`, `audience`, `as_of`, `status`, `provenance`, and the
  `not_human_reviewed` caveat when it applies);
- `navigation`: output pages and labels, independently of the source map;
- `assets`: the only files or directories copied to declared output paths;
- the output directory, stylesheet route, shell copy and optional section-link
  target.

Complete block-level `<svg>…</svg>` is the sole raw-markup passthrough. It must
have a `viewBox` and accessible name; scripts, event handlers, embedded styles,
foreign objects and external fetches are rejected. Markdown links to declared
pages are rewritten from `.md` source routes to their configured `.html`
outputs.

## Where to start

The report is written as a technical reference, not as an introduction. If you
want the argument rather than the specification:

- **§1–§3** give the component model and the consolidation channels
  (C-N / C-X / C-T / C-S), which is the part most relevant to current AI.
- **§9** is the list of falsifiable claims. It is the shortest route to
  understanding what the framework commits to.
- The glossary entry for a term is usually clearer than the report's first use
  of it.

## Related work

- **[retention-bench](https://github.com/symbolfarm/retention-bench)** — a
  research instrument for measuring whether what a system learned survives a
  discontinuity that erases working state. It is the measurement side of the
  consolidation claims here.
- **constructive-retention** — experiments in constructive algorithms for
  memory consolidation. In progress, not yet public.
- **adus-harness** — an agent harness designed explicitly around the ADUS
  components. In early scoping, not yet public.

## Status

Independent research, actively revised. The framework is a working instrument
rather than a settled result: version numbers move, claims are reformulated
when they turn out not to discriminate, and the v1.3 → v1.4 changelog is a fair
sample of how much can change between versions.

Feedback and criticism are welcome — the claims in §9 are stated to be
falsifiable, and finding one false is useful.

## Citation

```
@techreport{ADUSv1_4,
  title  = {{ADUS: A Functional Architecture of Intelligence (v1.4)}},
  author = {{Toby Lightheart}},
  url    = {https://github.com/tobylightheart/adus-intelligence},
  year   = {2026}
}
```
