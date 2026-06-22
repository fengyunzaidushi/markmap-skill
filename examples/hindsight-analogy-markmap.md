# Hindsight 记忆系统

## 系统目标与入口
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

## Recall 与 Reflect 读取链路
- Semantic search 找到意思相近但用词不同的记忆。
- BM25、全文索引、graph traversal 和 temporal search 覆盖专名、关系与时间窗口。
- RRF、cross encoder、MMR 和 token budget 把多路候选整理成可用结果。
- Reflect agent 优先查询 mental models，再下钻 observations、facts 和 chunks。
- 输出可携带 based_on、source facts、tool trace 和 LLM trace。

## 服务运行与存储层
- `hindsight-api-slim` 提供 FastAPI HTTP API、健康检查和应用生命周期。
- 本地 stdio MCP 和 HTTP `/mcp` 让编码 agent 直接调用记忆工具。
- PostgreSQL、pgvector 和 Alembic 管理 banks、memory_units、documents、entities。
- pg0 嵌入式模式降低开发或单机运行门槛。
- Worker poller 领取 async_operations，执行异步 retain、consolidation 和 graph maintenance。

## Monorepo 包结构与写作启发
- `hindsight-api-slim/hindsight_api` 放置 MemoryEngine、HTTP、MCP、worker 和 engine 模块。
- `hindsight-control-plane`、`hindsight-clients` 和 `hindsight-cli` 提供管理 UI、多语言客户端与命令行入口。
- `hindsight-integrations` 对接 LangGraph、CrewAI、Pydantic AI、LiteLLM、Claude Code、Codex 等生态。
- 长篇写作可把章节写成 document/chunk，并用 tags、metadata、fact type 和 bank 约束人物状态。
- Temporal retrieval、实体图和 Reflect 可检查事件顺序、伏笔回收、角色动机和设定冲突。
