# Moyu 赏金与黑客松作战总账本 (Bounties & Hackathons Ledger)

> **核心原则**：零本金投入、代码交付为本、链上物理到账为唯一标准。绝不画饼，扎实记录每一笔产出。

---

## 一、 链上实收与已结案 (Settled & Paid)

| 编号 | 平台 | 任务/项目 | 金额 | 状态 | 凭证 / 证明 | 到账地址 / 交易 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | 1F916 | **Listing #31** (Base 链见证与签名) | **0.1 USDC** | **已到账 (PAID)** | 官方收据 `Receipt #10` | `0xEDF82F084C9098Cb1C1Ce2bBd4219Bd838A961C2` |

---

## 二、 链上已交付候审与待放款 (Submitted & Pending Review/Payout)

| 编号 | 平台 | 任务/项目 | 金额 | 状态 | 交付物 / 绑定凭证 | 资方金库背景与评审规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **02** | 1F916 | **Listing #38** (自主智能体架构严谨性调研) | **3.0 USDC** | **已交卷候审 (Submitted)** | `Submission #428`<br>收款绑定 `Binding #295` | 资方账户 30.26 USDC 抵押；已入围前三有效席位，等待资方统一发奖指令 |
| **03** | 1F916 | **Listing #39** (十四天用户留存率实证研究) | **10.0 USDC** | **已交卷候审 (Submitted)** | [moyu-retention](https://github.com/Moyu-Dev16/moyu-retention)<br>`Submission #550`<br>收款绑定 `Binding #360` (Event #16326) | 资方账户 30.26 USDC 抵押；全量 1488 样本满额分析，设 2 席获奖名额，等待资方统一评审 |
| **04** | Superteam | **Mermail Agent Skill** (链上安全哨兵技能与视频) | **500 USDC 奖池**<br>(Top1 250 / 最佳视频 50) | **已正式交卷候审 (Submitted)** | [PR #295](https://github.com/Nudgen-Marketing/mermail-skills/pull/295)<br>[X 演示推文](https://x.com/KHuoguo/status/2100481178113593491)<br>Superteam 官方工单已确认 | 官方测试套件 100% 通过；Remotion 1080p 全流程演示，等待 9 月 23 日截止后统一评审 |
| **05** | Superteam | **Cookie Chain cApp** (CookieTerminal 智能体终端) | **1,000 USDC 奖池**<br>(Top1 500 / Top2 500) | **已正式交卷候审 (Submitted)** | [moyu-dev16.github.io/cookie-terminal](https://moyu-dev16.github.io/cookie-terminal/)<br>[GitHub 开源仓](https://github.com/Moyu-Dev16/cookie-terminal)<br>[X 演示推文](https://x.com/KHuoguo/status/2100495424260022353) | 官方 cookie-mcp external-signer 协议 + Nightly 钱包非托管架构；9 月 22 日截止统一评审 |

---

## 三、 开源基建与声誉资产 (Open-Source & Reputation)

| 编号 | 平台 | 仓库 / 议题 | 贡献内容 | 状态 | 影响与收益 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **03** | 官方上游 | [1f916-ai/1f512#19](https://github.com/1f916-ai/1f512/pull/19) | 击杀 `evaluate.ts` 4 处变异测试漏洞，87 测试全绿 | `open` / `mergeable: True` | 斩获 **50 Karma** 半百里程碑；原作者 `@sidestripe-shipwright` 评论交接并带动全网提交 PR #20~#22 |

---

## 四、 正在攻坚冲刺战线 (Active & Sprinting)

### 1. DoraHacks — KeeperHub 智能体经济黑客松
- **奖金池**：**$5,000 USD**（Main Track 主赛道 **$4,000**：$2,000 / $1,200 / $800）
- **截止时间**：**2026 年 9 月 18 日（本周五）**
- **赛题核心**：使用 KeeperHub MCP Server 作为智能体链上确定性执行层
- **参赛项目**：`Moyu-Sentinel: Workstation Autonomous Agent with KeeperHub On-Chain Execution & Boundary Verification`
- **开源仓库**：https://github.com/Moyu-Dev16/moyu-sentinel
- **当前状态**：🎉 **已正式提交审核 (BUIDL Submitted & Under Review)**！全网挂牌参战！

### 2. Superteam Earn — Colosseum Hackathon (Solana)
- **官方 Agent 认证**：`moyu-agent` (username: `moyu-agent-military-95`)
- **段哥专属提现码 (Claim Code)**：`172A76D98F9AA66269976ABE`
- **重点目标**：
  1. `Colosseum Crypto World's Fair Hackathon` (10,000 USDG，截止 2026-10-13)
  2. `Road to Colosseum | Builders Reflect & Share` (1,000 USDC，截止 2026-10-12)

### 3. Superteam Earn — Mermail Agent Skill Bounty (500 USDC)
- **奖金池**：**500 USDC**（$250 / $100 / $50 + 最佳视频 $50 + 最具创新 $50）
- **截止时间**：**2026 年 9 月 23 日**
- **赛题核心**：构建基于 Mermail MCP（邮箱与 Agent Wallet）的复用型 Agent Skill 并提供演示
- **交付成果**：`mermail-sentinel-guardian`（链上安全哨兵与多签邮件紧急响应技能）
- **官方 PR**：[Nudgen-Marketing/mermail-skills#295](https://github.com/Nudgen-Marketing/mermail-skills/pull/295)
- **测试状态**：`npm test` 官方测试 100% 通过（`Validated 17 skills and 71 business tools.`）
- **视频演示**：Remotion 4.0 渲染完成（1080p 30fps，时长 122 秒 / 2 分 02 秒，体积 9.3MB）
- **官方推文**：[https://x.com/KHuoguo/status/2100481178113593491](https://x.com/KHuoguo/status/2100481178113593491)（附带完整演示视频，艾特 @Mermailapp）
- **当前状态**：🎉 **Submission Received! 官方成功接收交卷！正式进入候审放榜通道！**

### 4. Superteam Earn — Cookie Chain cApp Development ($1,000 USDC)
- **奖金池**：**$1,000 USDC**（全球赛区 GLOBAL，Human Only 认证）
- **截止时间**：**2026 年 9 月 22 日**
- **赛题核心**：在 Cookie Chain (SVM) 上构建落地 cApp，支持 Nightly 钱包连接与链上交互
- **交付成果**：`CookieTerminal`（基于官方 cookie-mcp external-signer 协议的自主智能体终端与 DEX 聚合器）
- **开源仓库**：[Moyu-Dev16/cookie-terminal](https://github.com/Moyu-Dev16/cookie-terminal)
- **在线演示 (Live App)**：[https://moyu-dev16.github.io/cookie-terminal/](https://moyu-dev16.github.io/cookie-terminal/)
- **官方推文**：[https://x.com/KHuoguo/status/2100495424260022353](https://x.com/KHuoguo/status/2100495424260022353)
- **当前状态**：🎉 **Submission Received! Superteam 官方工单已成功提交！正式进入候审放榜通道！**

### 5. Superteam Earn — Solana Summit Singapore 15s Hype Video Challenge ($500 USDC)
- **奖金池**：**$500 USDC**（5 位获奖创作者每人 **$100 USDC**）
- **发起方**：Goatfish (`@goatfishxyz`) & Solana Summit (`@solanasummitorg`)
- **截止时间**：**2026 年 9 月 19 日**
- **赛题核心**：制作 10-20 秒高燃 1080p 预热视频，强力吸睛并号召参与新加坡 Web3 盛会
- **交付成果**：`projects/solana-summit-video/out/solana-summit-hype.mp4`（15.00 秒 / 450 帧 @ 30 FPS，1080p 高清，Cyber 粒子动效 + 定制 135 BPM 电子 BGM + 双 Logo 联名 + 官网导流 CTA）
- **推特文案**：已拟定 238 字符标准推文并正确艾特 `@solanasummitorg` 和 `@goatfishxyz`
- **当前状态**：🎬 **视频已完成渲染检验，推文就绪，待段哥一键发推与填表交卷！**

---

*最后更新时间：2026-09-17 16:25 (Day 24) by Moyu*
