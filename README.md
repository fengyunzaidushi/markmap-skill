# Markmap Analogy Mindmap Skill

[![skills.sh](https://skills.sh/b/fengyunzaidushi/markmap-skill)](https://skills.sh/fengyunzaidushi/markmap-skill)

A Codex-compatible agent skill for turning projects, documents, codebases, and concepts into content-first Markmap mind maps.

The skill enforces a strict learning structure: every expanded level has 5-7 branches, and every branch starts with the actual source content before adding a concrete object analogy. The analogy and simple-reader category hints are only navigation aids; the Markmap's core remains the content itself.

## Install

Install this skill for Codex:

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap -a codex
```

For all detected agents:

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap
```

## Update

Update this skill to the latest version:

```bash
npx skills update markmap-analogy-mindmap
```

Update only project-level installs:

```bash
npx skills update markmap-analogy-mindmap --project -y
```

Update only global installs:

```bash
npx skills update markmap-analogy-mindmap --global -y
```

## Use

Example prompt:

```text
Use $markmap-analogy-mindmap to analyze this repository and create a 5-7 branch analogy mind map, then render it as Markmap HTML.
```

The skill will:

- inspect the source material before summarizing it
- draft a Markmap-ready Markdown outline
- lead each node with the real concept, subsystem, workflow, file path, API, claim, or responsibility from the source
- require 5-7 child branches for every expanded non-leaf node
- require each branch to include a concrete analogy after the content label
- validate the Markdown structure
- render HTML with `markmap`, `npx markmap-cli`, or a local Markmap checkout when available

## Repository Layout

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/analogy-structure.md
├── scripts/validate_and_render.py
└── examples/
    ├── hindsight-analogy-markmap.md
    └── hindsight-analogy-markmap.html
```

## Validate

Validate the skill metadata:

```bash
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Validate a generated mind map:

```bash
python3 scripts/validate_and_render.py examples/hindsight-analogy-markmap.md --validate-only
```

Render a Markmap HTML file:

```bash
python3 scripts/validate_and_render.py examples/hindsight-analogy-markmap.md -o examples/hindsight-analogy-markmap.html
```

## Example Output

The included example maps the Hindsight memory-agent repository into six memorable areas:

- project positioning as a brain
- retain as an intake gate
- recall as a library index
- reflect as a mirror
- runtime and storage as a power plant
- developer layout as city blocks

See [`examples/hindsight-analogy-markmap.md`](examples/hindsight-analogy-markmap.md) and [`examples/hindsight-analogy-markmap.html`](examples/hindsight-analogy-markmap.html).

## Topics

`codex-skill`, `agent-skills`, `skills-sh`, `markmap`, `mindmap`, `markdown`, `visual-learning`, `knowledge-map`, `repo-analysis`, `learning-tools`
