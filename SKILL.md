---
name: markmap-analogy-mindmap
description: Generate content-first Markmap mind maps from projects, documents, codebases, or concepts. Use when Codex needs to create a Markdown/HTML mind map that explains source material from whole to parts, keeps the real content as the structure, and limits leaf-detail groups to about 5-7 items for readability.
---

# Markmap Analogy Mindmap

Create a content-first Markmap-ready Markdown outline, validate its shape, and render it to HTML when requested or useful.

## Core Rules

- Structure from whole to parts: root purpose -> major real concepts -> workflows/modules/details.
- Use the source material itself as the map structure. Do not invent broad category headings just to make content easier for beginners.
- Remove category-only labels such as "项目定位", "运行机制", "开发版图", "核心概念", "主要模块", "使用场景", "overview", or "architecture" unless they are part of the source text.
- Do not require every level to have 5-7 branches. Let each level follow the real content.
- Keep leaf-detail groups readable: when a parent has only leaf children, use at most 7 children, preferably 5-7 when there are many details.
- If a topic has more than 7 leaf details, group them under meaningful source-based subtopics rather than listing everything flat.
- Analogies are optional. Use them only when they genuinely help memory, and keep them after the content label. Never let an analogy become the node's main point.
- Do not fake certainty about a project. Inspect README, docs, package files, tests, source directories, and local scripts before summarizing a repository.
- Keep generated Markdown concise enough for a mind map. Use short content labels and one evidence-grounded sentence where useful.

Read `references/analogy-structure.md` when designing a non-trivial map or when the source material is a repo/codebase.

## Workflow

1. Inspect the source material first.
   - For a repo, start with `README`, `AGENTS.md`/`CLAUDE.md`, package manifests, docs, and top-level directories.
   - For a document, identify the main thesis, sections, repeated concepts, and terms that need memory hooks.
2. Draft from global to local.
   - Use one H1 root that states the subject.
   - Use `##` for the main real content areas, not reader-friendly category buckets.
   - Start each branch with the actual concept, subsystem, claim, workflow, file path, API, or responsibility from the source.
   - Expand only where detail helps understanding. Do not force a fixed branch count at each level.
   - Keep leaf lists short. If a node has more than 7 leaf children, regroup the details into source-based subnodes.
3. Validate the Markdown with the bundled script:

```bash
python3 ~/.codex/skills/markmap-analogy-mindmap/scripts/validate_and_render.py input.md --validate-only
```

4. Render to Markmap HTML when an output artifact is expected:

```bash
python3 ~/.codex/skills/markmap-analogy-mindmap/scripts/validate_and_render.py input.md -o output.html
```

5. If validation fails, revise the outline. Do not bypass category-only or oversized leaf-list checks unless the user explicitly asks for a non-standard map.

## Markmap Rendering

The script tries these renderers in order:

1. `markmap` on `PATH`
2. `npx --yes markmap-cli`
3. a local checkout at `/root/markmap` if it has built CLI dependencies

If none are available, leave the validated Markdown as the deliverable and report that HTML rendering was unavailable.

## Output Standards

- Return the generated `.md` and `.html` paths when files are created.
- Mention any source paths inspected and any validation/render command results.
- Keep source repos read-only unless the user asks to modify them.
- For Chinese users, write the mind map in Chinese by default.
