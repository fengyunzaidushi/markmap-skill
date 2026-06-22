# Analogy Structure Guide

Use this reference when building a strict analogy mind map.

## Shape Contract

- One root heading is allowed to have 5-7 top-level children.
- Every expanded child must also have 5-7 children.
- A node with no children is a leaf and does not need 5-7 descendants.
- A node is "expanded" when it has nested headings or nested list items below it.
- Every non-root node must include a concrete analogy marker:
  - Chinese: `类比：头`, `类比：厨房`, `类比：车轮`
  - English: `Analogy: head`, `Analogy: kitchen`, `Analogy: wheel`

## Practical Depth

For codebases, use 2-4 visible levels unless the user asks for more. A useful default:

1. Root: project name and purpose.
2. Layer 1: 5-7 system areas.
3. Layer 2: 5-7 responsibilities inside each expanded system area.
4. Layer 3: only for areas where the source evidence is strong and memory value is high.

Do not force every leaf into deeper children. It is better to stop at a validated 2-level map than to invent details.

## Analogy Frames

Choose frames that help recall the parent concept:

- Product/repo overview: body, city, workshop, airport, library, factory, ship.
- Runtime architecture: power grid, kitchen line, railway station, nervous system, control tower.
- API surface: restaurant menu, reception desk, tool wall, vending machine, switchboard.
- Data/storage: warehouse, filing cabinet, pantry, bank vault, library shelves.
- Developer workflow: toolbox, assembly line, checklist board, repair bench, test track.
- UI/application shell: cockpit, dashboard, storefront, map, control room.

Avoid abstract analogies like "strategy", "capability", "module", "pipeline" as the object itself. The analogy must be a specific thing someone can picture.

## Branch Writing Pattern

Use compact, scannable lines:

```markdown
# Hindsight 架构记忆图

## 记忆核心（类比：大脑）
- Retain 写入（类比：记事本）：把事实、上下文和时间送入记忆库。
- Recall 检索（类比：图书索引）：按问题找回相关记忆。
- Reflect 反思（类比：镜子）：基于已有记忆生成洞察。
- Banks 隔离（类比：抽屉柜）：用 bank_id 分隔不同记忆空间。
- Metadata 过滤（类比：标签贴）：用属性约束检索范围。
```

The parent has exactly five children. Each child has a visible object analogy.

## Repo Mapping Heuristic

When mapping a repository:

- Start from user-facing purpose in `README`.
- Use package manifests and top-level folders to decide the 5-7 first-layer branches.
- Use docs and tests to fill second-layer responsibilities.
- Prefer "what this area does" over file-by-file inventory.
- Mention exact packages or directories only when they help the user navigate.
- Preserve uncertainty: if a directory is present but not inspected deeply, label it as "entry point" or "surface" rather than claiming implementation behavior.

## Repair Rules

If validation reports too few or too many children:

- Too few: split a broad branch into separate concrete responsibilities found in source evidence.
- Too many: merge small details into the sentence text of a sibling branch.
- Missing analogy: add a physical object that matches the child role, not the parent role.
- Inconsistent depth: convert weak deep nodes into inline text, or expand them to 5-7 children only when evidence supports it.
