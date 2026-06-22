# Hindsight 项目记忆地图

## 项目定位（类比：大脑）
- 长期记忆系统（类比：海马体）：Hindsight 让 agent 学会保留事实、经历和长期形成的理解，而不是只保存聊天记录。
- 三类记忆（类比：三层书架）：world facts、experience facts、mental models 分别承载通用事实、个人经历和归纳后的模型。
- Memory bank（类比：抽屉柜）：bank_id 把不同用户、agent、项目或场景的记忆空间隔离开。
- 三个主动作（类比：呼吸节奏）：Retain 写入、Recall 找回、Reflect 综合推理，形成最小闭环。
- 目标场景（类比：随身笔记本）：面向需要长期连续任务的 AI agent，尤其适合保存偏好、上下文和任务经验。

## Retain 写入链路（类比：收件口）
- 内容接收（类比：邮箱投递口）：HTTP、MCP、SDK 或 CLI 把文本、文档、事件送入指定 bank。
- 文档分块（类比：切片面包机）：大文档会被切成 chunks，保留原文上下文供后续展开。
- 事实抽取（类比：筛网）：LLM 或规则从内容中提取事实、时间、实体和关系。
- 实体链接（类比：红线板）：entity resolver 和 link utils 把人物、组织、地点、概念连成图。
- 后台维护（类比：夜班整理员）：retain 后可触发 consolidation 和 graph maintenance，把零散事实整理成 observations。

## Recall 检索链路（类比：图书馆索引）
- 语义检索（类比：同义词词典）：semantic search 找到意思相近但用词不同的记忆。
- 关键词检索（类比：姓名牌）：BM25 或全文索引确保专名、术语和唯一标识不会丢。
- 图检索（类比：地铁换乘图）：graph traversal 沿实体关系找到间接相关事实。
- 时间检索（类比：日历）：temporal search 解析去年、春天、某日之前之后等时间窗口。
- 融合重排（类比：评审席）：RRF、cross encoder、MMR 和 token budget 把多路候选整理成可用结果。

## Reflect 反思链路（类比：镜子）
- 工具循环（类比：侦探工具箱）：reflect agent 用只读工具反复查询 mental models、observations、facts 和 chunks。
- 先查模型（类比：地图总览）：系统优先使用 mental models，先看长期归纳，再下钻原始事实。
- 再查观察（类比：便签墙）：observations 提供比单条事实更高层的总结和判断。
- 原文展开（类比：放大镜）：expand 或 include chunks 用来找回生成事实时的原文细节。
- 有据回答（类比：庭审证物）：reflect 输出可携带 based_on、source facts、tool trace 和 LLM trace。

## 运行与存储（类比：发电厂）
- FastAPI 服务（类比：总闸）：`hindsight-api-slim` 提供 HTTP API、健康检查和应用生命周期。
- MCP 服务（类比：工具插座）：本地 stdio MCP 和 HTTP `/mcp` 让编码 agent 直接调用记忆工具。
- PostgreSQL 存储（类比：仓库）：默认使用 PostgreSQL、pgvector 和 Alembic 迁移管理 banks、memory_units、documents、entities。
- pg0 嵌入式模式（类比：便携电池）：开发或单机运行时可使用嵌入式 PostgreSQL，降低部署门槛。
- Worker 任务（类比：传送带）：后台 poller 领取 async_operations，执行异步 retain、consolidation 和 graph maintenance。

## 开发版图（类比：城市街区）
- API 核心区（类比：市政厅）：`hindsight-api-slim/hindsight_api` 放置 MemoryEngine、HTTP、MCP、worker 和 engine 模块。
- 控制台区（类比：驾驶舱）：`hindsight-control-plane` 是 Next.js 管理 UI，用来观察和操作系统。
- 文档区（类比：图书馆）：`hindsight-docs` 用 Docusaurus 承载开发者文档、SDK 文档和指南。
- 客户端区（类比：公交站）：`hindsight-clients` 和 `hindsight-cli` 提供 Python、TypeScript、Rust、Go 与命令行入口。
- 集成区（类比：港口）：`hindsight-integrations` 对接 LangGraph、CrewAI、Pydantic AI、LiteLLM、Claude Code、Codex 等生态。

## 对长篇小说记忆 Agent 的启发（类比：作家工作室）
- 章节入库（类比：稿纸盒）：把每章正文作为 document/chunk 写入，保留可展开原文。
- 角色正典（类比：人物卡）：用 tags、metadata、fact type 和 bank 约束人物、阵营、关系与状态。
- 时间线一致性（类比：墙上年表）：利用 temporal retrieval 检查事件顺序、年龄、伏笔和回收节点。
- 伏笔追踪（类比：线轴）：实体图和关系链接可帮助追踪道具、承诺、秘密和因果关系。
- 写作反思（类比：编辑桌）：Reflect 可封装成检查角色动机、剧情矛盾、设定冲突和章节摘要的只读助手。
