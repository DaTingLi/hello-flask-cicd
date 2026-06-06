# PROGRESS · hello-flask-cicd 〔本项目活记忆 · 状态机〕

> **作用**:这是项目的"存档点"。任意 AI、任意重启会话,读它即可知道当前做到哪、下一步做什么、踩过什么坑。
> **更新时机**:每完成一个有意义步骤、每次会话结束前。

---

## 当前状态 (最后更新: 2026-06-06 · by AI)

- **阶段**: 开发中
- **上一步完成**: GitHub Secrets 配置完成
- **下一步 (TODO 第一条)**: 从 main 开第一条 feature 分支
- **阻塞项**: 无

---

## 待办清单 (TODO,按优先级)

- [x] 初始化 Git 仓库: `git init`
- [x] 创建 GitHub 远程仓库并关联: https://github.com/DaTingLi/hello-flask-cicd
- [x] 配置 GitHub Secrets (SSH_PRIVATE_KEY, SSH_HOST, SSH_USER)
- [ ] 从 main 开第一条 feature 分支: `feature/1-welcome-endpoint`
- [ ] 实现欢迎接口: GET / 返回欢迎 JSON
- [ ] 实现健康检查接口: GET /health 返回 {"status":"ok"}
- [ ] 编写单元测试 (覆盖率≥80%)
- [ ] 配置开发依赖: requirements.txt + requirements-dev.txt
- [ ] 编写 Dockerfile
- [ ] 编写 CI workflow (.github/workflows/ci.yml)
- [ ] 编写 CD workflow (.github/workflows/cd.yml)
- [ ] 本地自检: ruff format + ruff check + pytest
- [ ] 提交并推送 feature 分支
- [ ] 创建 PR,等待 CI 全绿
- [ ] 人工审核后合并 main,触发 CD
- [ ] 验证部署成功与健康检查
- [ ] 会话结束前更新本文件

---

## 关键决策记录 (ADR)

| 日期 | 决策 | 理由 |
|---|---|---|
| 2026-06-06 | 选择 Python 3.11 + Flask | 教学常用、轻量级 |
| 2026-06-06 | 使用 ruff 替代 black/flake8 | 现代化、快速 |
| 2026-06-06 | 端口预留 8000-8100 区间 | 支持回退 |
| 2026-06-06 | 仓库名定为 hello-flask-cicd | hello-flask 已被占用 |

---

## 已知坑 (GOTCHAS)

- 待记录

---

## 里程碑 (DONE)

- [x] 项目框架搭建完成
- [x] Git 仓库初始化并推送到 GitHub (hello-flask-cicd)
- [ ] 欢迎接口实现并通过测试
- [ ] 健康检查接口实现并通过测试
- [ ] CI/CD 流水线跑通
- [ ] 部署成功并验证健康检查
