# 01 · 需求 / 活 PRD 〔本项目活记忆 · AI 维护〕

> **作用**:这是本项目唯一的需求文档。所有新功能、缺陷、技术债都追加到这里,不要另起多个 PRD 文件。
> **更新时机**:每次有新需求、需求变更、验收标准变化时更新。

---

## 1. 需求来源

| 类型 | 来源 | 进入方式 |
|---|---|---|
| 功能需求 Feature | 学习目标 | 写成用户故事 |
| 缺陷 Bug | 测试/日志 | 写复现步骤 |
| 技术债 Tech Debt | 开发/CI/CD | 写影响和修复目标 |

---

## 2. Issue 生命周期

| 阶段 | 状态 | 动作 |
|---|---|---|
| 提出 | Open | 写清场景、目标、验收标准 |
| 排期 | Backlog/Todo | 决定优先级和负责人 |
| 开发 | In Progress | 从 main 开 feature 分支 |
| 评审 | In Review | 提 PR,等待 CI 和 Review |
| 合并 | Done | PR 合并 main,自动关闭 Issue |
| 验收 | Verified | 按验收标准确认 |

---

## 3. 用户故事模板

```text
### US-<编号> <一句话标题> · 状态: <Backlog/In Progress/Done>
作为 <角色>,
我想要 <能力>,
以便 <价值>。

验收标准:
- AC1: Given <前提>,When <动作>,Then <可验证结果>。
- AC2: <补充标准>

技术备注:
- <可选:约束、边界、风险>
```

---

## 4. 需求清单

### US-1 欢迎接口 · 状态: Backlog

作为 **API 用户**,
我想要 **访问 GET /**,
以便 **收到友好的欢迎响应**。

验收标准:
- AC1: Given 服务正常运行,When 请求 GET /,Then 返回 200 状态码和 JSON 格式的欢迎消息。
- AC2: Given 响应是 JSON,When 解析响应体,Then 包含 `message` 字段且非空。
- AC3: Given 响应头,When 检查 Content-Type,Then 为 `application/json`。

技术备注:
- 欢迎消息建议格式: `{"message": "Welcome to Hello Flask!"}`

---

### US-2 健康检查接口 · 状态: Backlog

作为 **部署系统/监控服务**,
我想要 **访问 GET /health**,
以便 **验证服务可用性**。

验收标准:
- AC1: Given 服务正常运行,When 请求 GET /health,Then 返回 200 状态码。
- AC2: Given 响应是 JSON,When 解析响应体,Then 包含 `{"status": "ok"}`。
- AC3: Given 响应头,When 检查 Content-Type,Then 为 `application/json`。
- AC4: Given 响应速度,When 请求 /health,Then 在 100ms 内返回(用于轻量级探测)。

技术备注:
- 健康检查必须轻量，不查询数据库/外部服务
- 供 k8s/云平台/CD 部署后自动验证

---

### US-3 CI/CD 流水线 · 状态: Backlog

作为 **项目开发者**,
我想要 **自动化 CI 检查与 CD 部署**,
以便 **每次代码变更都自动验证并上线**。

验收标准:
- AC1: Given PR 创建,When 推送 feature 分支,Then CI 自动执行格式、lint、测试、构建检查。
- AC2: Given CI 通过,When 合并到 main,Then CD 自动部署到服务器。
- AC3: Given 部署完成,When 执行健康检查,Then /health 返回 `{"status": "ok"}`。
- AC4: Given CI 检查,When 查看日志,Then 包含 ruff format、ruff check、pytest、docker build 步骤。
- AC5: Given CD 部署,When 查看日志,Then 打印最终访问地址(含端口)。

技术备注:
- CI: 格式、静态检查、单元测试(覆盖率≥80%)、Docker 构建
- CD: SSH 部署、容器重启、健康检查
- Secrets 需要: SSH_PRIVATE_KEY、SSH_HOST、SSH_USER

---

## 5. 非功能需求

- **安全**: 密钥只进 Secrets，不进 Git
- **可维护**: 一需求一小 PR，避免大爆炸式提交
- **可测试**: 核心逻辑必须有单元测试
- **可部署**: 部署后必须有健康检查
