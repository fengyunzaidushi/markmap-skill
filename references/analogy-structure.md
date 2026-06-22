# Content-First Markmap Structure Guide

Use this reference when building a non-trivial Markmap from a repository, document, or concept.

## Principle

The mind map is about the source material. It should help a reader move from the whole system to local details.

- Start with the subject's real purpose.
- Expand into real concepts, modules, workflows, APIs, files, decisions, or claims.
- Avoid category headings that only describe the reader experience, such as "overview", "architecture", "main modules", "core concepts", "project positioning", or "use cases".
- Use analogies only as optional memory hooks after the content label.
- Keep leaf-detail groups short enough to scan.

## Shape Contract

- Exactly one root H1.
- Any number of meaningful main branches is allowed.
- A non-leaf node may have fewer than 5 or more than 7 children when the source structure requires it.
- A node whose children are all leaves must have at most 7 children.
- When a parent has many leaf details, prefer 5-7 leaves. If there are more than 7 details, create meaningful subnodes based on the source.
- Every non-root node should contain substantive content, not a generic category label.

## Whole-To-Part Order

For codebases, a useful default:

1. Root: project name and one-line purpose.
2. Main layer: real system concepts or package/workflow areas from the repository.
3. Second layer: responsibilities, APIs, commands, files, or data structures under each area.
4. Third layer: only when detail materially helps the reader understand or remember the system.

For articles or documents:

1. Root: the thesis or title.
2. Main layer: actual arguments, stages, or sections.
3. Second layer: evidence, examples, mechanisms, or implications.
4. Leaf layer: only the most important details.

## Good And Weak Patterns

Good:

```markdown
# Hindsight 记忆系统

## Retain 写入链路
- HTTP/MCP/SDK 入口：把文本、文档和事件送入指定 memory bank。
- 文档与 chunk：保留原文上下文，支持后续展开。
- 事实抽取：从内容中提取事实、时间、实体和关系。
- 实体链接：把人物、组织、地点和概念连成图。
- 后台维护：触发 consolidation 与 graph maintenance。
```

Weak:

```markdown
# Hindsight 记忆系统

## 运行机制
- 核心概念：介绍系统是什么。
- 主要流程：介绍系统怎么跑。
- 使用场景：介绍能做什么。
```

The weak version is easy to read but loses the actual content. Rewrite category nodes into source terms.

## Repo Mapping Heuristic

When mapping a repository:

- Start from the user-facing purpose in `README`.
- Use package manifests, docs, tests, and top-level folders to decide main branches.
- Prefer "what this area does" over file-by-file inventory.
- Mention exact packages or directories only when they help navigation.
- Name nodes with actual repository terms: package names, operations, APIs, storage objects, command names, docs concepts, or verified behaviors.
- Preserve uncertainty: if a directory is present but not inspected deeply, label it as an entry point or surface rather than claiming implementation behavior.

## Repair Rules

If validation reports issues:

- Too many leaf children: group details under source-based subtopics.
- Generic category node: replace it with the actual content concept.
- Thin branch: merge it into a sibling sentence unless it has enough source-backed detail to expand.
- Inconsistent depth: shallow is acceptable when the source does not justify deeper structure.
- Missing root: add one H1 with the subject and purpose.
