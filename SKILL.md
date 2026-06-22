---
name: markmap-analogy-mindmap
description: 生成以内容为主的 Markmap 思维导图，用于项目、文档、代码库或概念梳理。Use when Codex needs to create Markdown/HTML mind maps that explain source material from whole to parts, keep real content as the structure, and limit leaf-detail groups to about 5-7 items for readability.
---

# 内容优先 Markmap 思维导图

把项目、文档、代码库或概念整理成可以用 Markmap 渲染的 Markdown，并在需要时校验结构、生成 HTML。

## 核心规则

- 先整体后局部：根主题说明对象和目的，再展开真实主概念、流程、模块和细节。
- 用材料本身组织导图。不要为了照顾小白阅读而发明空泛分类标题。
- 去掉只起分类作用的标题，例如“项目定位”“运行机制”“开发版图”“核心概念”“主要模块”“使用场景”等，除非这些词本来就是原文的一部分。
- 不要求每一层都是 5-7 个分支。层级和分支数量应服从真实内容结构。
- 只控制叶子明细组的可读性：当一个父节点下面全是叶子节点时，最多 7 项；如果细节很多，优先控制在 5-7 项。
- 如果某个主题超过 7 个叶子细节，按材料里的真实子主题继续分组，不要平铺所有条目。
- 类比是可选的。只有确实帮助记忆时才使用，并放在内容标签之后；不能让类比变成节点主体。
- 不要编造确定性。总结仓库前先看 README、文档、包配置、测试、源码目录和本地脚本。
- 保持导图简洁。节点用短内容标签，必要时补一句有依据的说明。

处理复杂仓库或长文档时，先读 `references/analogy-structure.md`。

## 工作流程

1. 先检查材料。
   - 仓库：先看 `README`、`AGENTS.md`/`CLAUDE.md`、包配置、文档和顶层目录。
   - 文档：先找主题、主张、章节、重复概念和需要记忆的术语。
2. 从整体到局部起草 Markdown。
   - 使用一个 H1 根标题说明对象。
   - 使用 `##` 展开真实内容主干，不使用“给读者看的分类桶”。
   - 每个节点优先写材料中的真实概念、系统、流程、文件路径、API、主张或职责。
   - 只在细节能帮助理解时继续展开，不强行凑固定分支数。
   - 叶子列表保持短。如果一个节点超过 7 个叶子节点，按真实子主题重新分组。
3. 用脚本校验 Markdown：

```bash
python3 ~/.codex/skills/markmap-analogy-mindmap/scripts/validate_and_render.py input.md --validate-only
```

4. 需要交付 HTML 时，渲染 Markmap：

```bash
python3 ~/.codex/skills/markmap-analogy-mindmap/scripts/validate_and_render.py input.md -o output.html
```

5. 如果校验失败，先修导图结构。除非用户明确要求非标准导图，否则不要绕过“空泛分类”和“叶子组过长”检查。

## Markmap 渲染

脚本会按顺序尝试：

1. `markmap`
2. `npx --yes markmap-cli`
3. 本机 `/root/markmap` 里的已构建 CLI

如果没有可用渲染器，就把已通过校验的 Markdown 作为交付物，并说明 HTML 未生成。

## 输出要求

- 创建文件后，返回 `.md` 和 `.html` 路径。
- 说明检查过哪些来源，以及校验/渲染命令结果。
- 除非用户要求修改源仓库，否则只读源材料。
- 中文用户默认输出中文导图；只有命令、路径、API、包名、术语必须保留英文时才用英文。
