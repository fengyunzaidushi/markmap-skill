# Hindsight 记忆系统

## 系统目标
- 为 AI agent 提供长期记忆，而不是只保存聊天记录。
- 把输入内容加工成事实、经历、实体、关系、时间线、观察与 mental models。
- 通过 memory bank 隔离不同用户、agent、项目或场景。
- 对外提供 HTTP API、MCP、SDK、CLI、控制台 UI 和嵌入式 Python API。
- 支持需要长期上下文的连续任务，例如个性化助手、代码 agent 和长篇写作助手。

## Retain 写入链路
- HTTP、MCP、SDK 或 CLI 把文本、文档、事件送入指定 bank。
- 大文档会被切成 chunks，保留原文上下文供后续展开。
- LLM 或规则从内容中抽取事实、时间、实体和关系。
- entity resolver 与 link utils 把人物、组织、地点、概念连成图。
- retain 后可触发 consolidation 和 graph maintenance，把零散事实整理成 observations。

## Recall 检索链路
- Semantic search 找到意思相近但用词不同的记忆。
- BM25 或全文索引确保专名、术语和唯一标识不会丢。
- Graph traversal 沿实体关系找到间接相关事实。
- Temporal search 解析去年、春天、某日之前之后等时间窗口。
- RRF、cross encoder、MMR 和 token budget 把多路候选整理成可用结果。

## Reflect 反思链路
- Reflect agent 使用只读工具查询 mental models、observations、facts 和 chunks。
- 系统优先使用 mental models，再下钻 observations 和原始事实。
- expand 或 include chunks 找回生成事实时的原文细节。
- Directives 和 bank config 影响回答风格、工具顺序和可用范围。
- 输出可携带 based_on、source facts、tool trace 和 LLM trace。

## 服务运行与存储层
- `hindsight-api-slim` 提供 FastAPI HTTP API、健康检查和应用生命周期。
- 本地 stdio MCP 和 HTTP `/mcp` 让编码 agent 直接调用记忆工具。
- PostgreSQL、pgvector 和 Alembic 管理 banks、memory_units、documents、entities。
- pg0 嵌入式模式降低开发或单机运行门槛。
- Worker poller 领取 async_operations，执行异步 retain、consolidation 和 graph maintenance。

## Monorepo 包结构
- `hindsight-api-slim/hindsight_api` 放置 MemoryEngine、HTTP、MCP、worker 和 engine 模块。
- `hindsight-control-plane` 是 Next.js 管理 UI。
- `hindsight-docs` 用 Docusaurus 承载开发者文档、SDK 文档和指南。
- `hindsight-clients` 和 `hindsight-cli` 提供 Python、TypeScript、Rust、Go 与命令行入口。
- `hindsight-integrations` 对接 LangGraph、CrewAI、Pydantic AI、LiteLLM、Claude Code、Codex 等生态。

## 长篇小说记忆 Agent 启发
- 每章正文可以作为 document/chunk 写入，保留可展开原文。
- tags、metadata、fact type 和 bank 可约束人物、阵营、关系与状态。
- Temporal retrieval 可检查事件顺序、年龄、伏笔和回收节点。
- 实体图和关系链接可追踪道具、承诺、秘密和因果关系。
- Reflect 可封装成检查角色动机、剧情矛盾、设定冲突和章节摘要的只读助手。
