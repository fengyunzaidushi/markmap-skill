---
name: markmap-analogy-mindmap
description: Generate memory-friendly Markmap mind maps from projects, documents, codebases, or concepts. Use when Codex needs to create a Markdown/HTML mind map with strict 5-7 child branches per expanded level and concrete object analogies for every branch, especially for learning, explaining architecture, summarizing repositories, or turning long material into visual memory aids.
---

# Markmap Analogy Mindmap

Create a content-first Markmap-ready Markdown outline, validate its shape, and render it to HTML when requested or useful.

## Core Rules

- Build every expanded non-leaf node with 5-7 child branches.
- Make the real source content the node title. The analogy is a small memory hook, never the main point.
- Give every branch a concrete object analogy after the content label using `（类比：<具体事物>）` or `(Analogy: <concrete object>)`.
- Do not use broad reader-friendly category labels as the main node text. Replace labels like "项目定位", "运行机制", "开发版图", or "核心概念" with the actual topic: e.g. `Hindsight 作为长期记忆系统`, `Retain 写入链路`, `Recall 多策略检索`, `hindsight-api-slim 服务入口`.
- Prefer familiar, physical objects that are easy to visualize: body parts, rooms, tools, vehicles, city facilities, factory stations, kitchen items, office objects, or map landmarks.
- Keep analogies local to the parent level. If one parent uses a "body" frame, its 5-7 children can be head, hands, torso, legs, feet, and senses; another parent can use a different frame such as a workshop or city.
- Do not fake certainty about a project. Inspect README, docs, package files, tests, source directories, and local scripts before summarizing a repository.
- Keep generated Markdown concise enough for a mind map. Use short content labels and push detail into one evidence-grounded sentence after the analogy.

Read `references/analogy-structure.md` when designing a non-trivial map or when the source material is a repo/codebase.

## Workflow

1. Inspect the source material first.
   - For a repo, start with `README`, `AGENTS.md`/`CLAUDE.md`, package manifests, docs, and top-level directories.
   - For a document, identify the main thesis, sections, repeated concepts, and terms that need memory hooks.
2. Draft a Markdown tree.
   - Use one H1 root.
   - Use `##` for the first map layer and deeper headings or nested lists for lower layers.
   - Start each branch with the actual concept, subsystem, claim, workflow, file path, API, or responsibility from the source.
   - Put learner-friendly category wording and concrete analogies after the content label.
   - Make every expanded node have 5-7 children. Collapse details into sentence text rather than adding arbitrary extra child nodes.
   - Add `类比：...` or `Analogy: ...` on every branch line.
   - Avoid category-only branches. A non-technical reader can use the analogy to orient, but the Markmap's core must remain the source content itself.
3. Validate the Markdown with the bundled script:

```bash
python3 ~/.codex/skills/markmap-analogy-mindmap/scripts/validate_and_render.py input.md --validate-only
```

4. Render to Markmap HTML when an output artifact is expected:

```bash
python3 ~/.codex/skills/markmap-analogy-mindmap/scripts/validate_and_render.py input.md -o output.html
```

5. If validation fails, revise the outline first. Do not bypass the branch-count or analogy checks unless the user explicitly asks for a non-standard map.

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
