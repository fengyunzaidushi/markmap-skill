# 内容优先 Markmap Skill

[![skills.sh](https://skills.sh/b/fengyunzaidushi/markmap-skill)](https://skills.sh/fengyunzaidushi/markmap-skill)

这是一个 Codex 可用的 agent skill，用来把项目、文档、代码库或概念整理成内容优先的 Markmap 思维导图。

它的重点不是用类别凑结构，而是让材料本身成为导图结构：先整体后局部，避免空泛分类标题，并把同一父节点下的叶子明细控制在最多 7 项，保证阅读时不散。

## 安装

只安装到 Codex：

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap -a codex
```

安装到所有检测到的 agent：

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap
```

## 更新

推荐刷新 Codex 安装：

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap -a codex -y --copy
```

刷新所有检测到的 agent：

```bash
npx skills add fengyunzaidushi/markmap-skill --skill markmap-analogy-mindmap --all --copy
```

如果当前项目的 `skills-lock.json` 状态正常，也可以尝试：

```bash
npx skills update markmap-analogy-mindmap
```

项目级和全局级快捷命令：

```bash
npx skills update markmap-analogy-mindmap --project -y
npx skills update markmap-analogy-mindmap --global -y
```

如果 `skills update` 出现 `Failed to check for deleted skills` 或 `Failed to update`，使用上面的 `skills add ... -y --copy` 刷新命令。

## 使用

示例提示词：

```text
使用 $markmap-analogy-mindmap 分析这个仓库，按先整体后局部生成内容优先的 Markmap HTML。
```

这个 skill 会：

- 先检查源材料，再总结。
- 起草 Markmap 可用的 Markdown。
- 让每个节点优先使用材料里的真实概念、系统、流程、文件路径、API、主张或职责。
- 避免空泛分类标题。
- 将叶子明细组控制在最多 7 项；细节很多时优先保留 5-7 项。
- 校验 Markdown 结构。
- 在可用时用 `markmap`、`npx markmap-cli` 或本机 Markmap checkout 渲染 HTML。

## 目录结构

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

## 校验

校验 skill 元数据：

```bash
python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

校验生成的思维导图：

```bash
python3 scripts/validate_and_render.py examples/hindsight-analogy-markmap.md --validate-only
```

渲染 Markmap HTML：

```bash
python3 scripts/validate_and_render.py examples/hindsight-analogy-markmap.md -o examples/hindsight-analogy-markmap.html
```

## 示例

仓库内置示例把 Hindsight 记忆系统从整体目标展开到具体工作流和包结构：

- Hindsight 作为长期记忆系统
- Retain、Recall、Reflect 工作流
- 服务运行与存储层
- monorepo 包结构
- 对长篇小说记忆 agent 的启发

见 [`examples/hindsight-analogy-markmap.md`](examples/hindsight-analogy-markmap.md) 和 [`examples/hindsight-analogy-markmap.html`](examples/hindsight-analogy-markmap.html)。

## Topics

`codex-skill`, `agent-skills`, `skills-sh`, `markmap`, `mindmap`, `markdown`, `content-first`, `knowledge-map`, `repo-analysis`, `learning-tools`
