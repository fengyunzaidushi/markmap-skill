# Content-First Markmap Skill

[![skills.sh](https://skills.sh/b/fengyunzaidushi/markmap-skill)](https://skills.sh/fengyunzaidushi/markmap-skill)

A Codex-compatible agent skill for turning projects, documents, codebases, and concepts into content-first Markmap mind maps.

The skill keeps the source material as the map structure. It works from whole to parts, avoids broad category headings, and keeps leaf-detail groups to at most 7 items so the result stays readable.

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

Reliable refresh command for Codex installs:

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap -a codex -y --copy
```

Reliable refresh command for all detected agents:

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap --all --copy
```

If the skill was installed with normal `skills` tracking and your project has a clean `skills-lock.json`, the shorter update command may also work:

```bash
npx skills update markmap-analogy-mindmap
```

Project-only and global-only update shortcuts:

```bash
npx skills update markmap-analogy-mindmap --project -y
npx skills update markmap-analogy-mindmap --global -y
```

If `skills update` fails with `Failed to check for deleted skills` or `Failed to update`, use the reliable `skills add ... -y --copy` refresh command above.

## Use

Example prompt:

```text
Use $markmap-analogy-mindmap to analyze this repository from whole to parts and render a content-first Markmap HTML.
```

The skill will:

- inspect the source material before summarizing it
- draft a Markmap-ready Markdown outline
- lead each node with the real concept, subsystem, workflow, file path, API, claim, or responsibility from the source
- avoid category-only headings
- keep leaf-detail groups to at most 7 items, preferably 5-7 when there are many details
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

The included example maps the Hindsight memory-agent repository from overall purpose into concrete workflows and packages:

- Hindsight as a long-term memory system
- Retain, Recall, and Reflect workflows
- service/runtime/storage layers
- monorepo packages
- implications for long-form novel memory agents

See [`examples/hindsight-analogy-markmap.md`](examples/hindsight-analogy-markmap.md) and [`examples/hindsight-analogy-markmap.html`](examples/hindsight-analogy-markmap.html).

## Topics

`codex-skill`, `agent-skills`, `skills-sh`, `markmap`, `mindmap`, `markdown`, `visual-learning`, `knowledge-map`, `repo-analysis`, `learning-tools`
