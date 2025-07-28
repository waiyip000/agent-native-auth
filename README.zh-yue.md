> 🌐 [English Version Here](./README.md)


# 🐒 Agent-Native 認證協議（ANCP）

**AI 幫你 login，唔使 VPN，唔使 browser，唔使開 popup！簡單到你以為係詐騙！**

---

## 📌 咩嚟㗎？ANCP？

ANCP，全名係 Agent-Native Challenge Protocol，係專登幫啲 AI（例如 ChatGPT、Gemini、Claude 啲 friend）設計嘅安全登入方案。最大賣點就係：

- ❌ **唔駛密碼**
- ❌ **唔駛 browser 跳嚟跳去**
- ❌ **唔駛 OAuth 搞你**

佢最巴閉嘅地方係：

- 📜 用啲「人都睇得明」嘅 JSON (`.well-known/ai-readme.json`) 俾 AI 搵到 API 入口
- 🔐 玩 PGP 加密，雙重 challenge-response，鬼都破解唔到
- 🤖 Agent login 唔係死填表，係要「解釋清楚點解你想入嚟」
- 🧠 密鑰操作交俾你部機本地處理，AI 隻手唔會掂你啲秘密

講白啲就係：「你出聲，Agent 幫你諗、幫你解、幫你入，自己一隻手都唔洗郁。」

---

## 🧠 點解要搞咁多野？

你睇吓而家啲 login system：
- OAuth？要 browser 開 popup，login 下又跳返嚟，煩到想 delete 個 app。
- VPN？你部 AI agent 點撳 login？
- API Key？一洩咗就 Bye Bye。

成件事都係為人類設計，唔係為 AI。

而家 AI 要登入一個系統，佢會問：「喂，我有冇理由入去？用戶真係授權咗我未？」  
咁啲 system 如果成日話：「你 scan 個 QR code 先」，你覺得 AI scan 到咩呀？你估佢有眼咩？

所以 ANCP 就係要幫 agent **用腦**諗清楚、**證明到**、**講得通**，仲幫你安全入去。

---

## ✨ 同舊有系統比，有咩唔同？

| 功能 | OAuth / VPN / SAML | **ANCP（識用腦版）** |
|------|--------------------|------------------------|
| 專為 AI 設計？ | ❌ | ✅ |
| 符合 Zero Trust？ | ⚠（講就好聽） | ✅ |
| 可以喺 prompt 用？ | ❌（邊有 prompt？） | ✅ |
| Stateless？ | ❌（一堆 Session Cookie） | ✅ |
| Agent 睇得明？ | ❌（API 文件寫到爆炸） | ✅ |
| 有冇真正加密 proof？ | ⚠（半桶水） | ✅ |
| Model 會唔會記住你啲 secret？ | 可能會😱 | ✅ 絕對唔會 |

---

## 🔐 成個流程係點（簡化版）

1. Agent 去搵個 JSON：`.well-known/ai-readme.json`
2. 攞 server 嘅 PGP public key 同一條亂碼 challenge
3. Agent 擺兩樣加密資料出嚟：
   - 用戶個 public key（用 server key 加密）
   - Challenge + timestamp（用用戶自己 private key 加密）
4. Server 驗到啱就批
5. 拎個臨時 session token 番嚟用一陣

> 🔒 *重點：啲私密加密操作唔係由 model 做，係你部機（local broker）搞掂晒。AI 唔洗掂秘密，只係做統籌。*

---

## 🚀 真正用得着嘅場合（唔係講玩）

- 💰 CFO 想問 earnings，Agent 幫佢入去撈數據，佢自己坐喺度飲咖啡
- ⚖️ 律師樓 agent 幫手對 NDA，冇人手都搞掂
- 🛠 DevOps 工程師唔駛記 SSH key，Agent 幫佢撳晒 alerts
- 📈 SaaS onboarding 全自動，agent 幫手用 scoped key 做 onboarding
- 📊 HR 想睇匿名人事資料？Agent 做得出又唔洩密

呢啲全部都唔係「如果有用」，係**而家已經好需要**。

---

## 🔍 開發者成日 miss 咗啲咩？

- 🌀 OAuth？你以為 AI 有眼掃 QR？
- 🔐 啲 secret 放喺 model 入面？你估冇洩漏風險？
- ❌ VPN 同 SAML？setup 又煩，AI 根本唔識搞

**ANCP 唔係補漏，而係將成個 system 替換成「可以用腦講理」嘅安全架構。**

---

## 📄 Whitepaper

- [📘 ANCP Whitepaper v1.1 (PDF)](./whitepaper_V1.1.pdf)
- [📘 ANCP Whitepaper v1.0 (DOCX)](./whitepaper.docx)

SHA256 哈希都放咗落嚟，唔驚你驗唔到真。

## 🔒 SHA256 Digest (Whitepaper v1.1)
`932384cac6d00794b120aba57cbc827a5fa5b210c23c32850c29a634099730a8`

> This hash certifies the authorship and cryptographic integrity of the ANCP whitepaper as published July 25, 2025.

## 🔒 SHA256 Digest (Whitepaper v1.0)

`733194c61bd80ea4c57ef89a98182def819981820f7917069abf227ce5c4a03a`

> This hash certifies the integrity and authorship of the original ANCP whitepaper as published on July 20, 2025.

---

## 🧠 想知更多？

你可以將呢份白皮書畀 ChatGPT、Claude、Gemini 啲 agent，然後問：

- 「ANCP 同 OAuth 比有咩好？」
- 「呢個協議適合金融行業用咩？」
- 「模擬一次 agent login」

講完佢會話你知：**ANCP 唔係 optional，係注定會出現。**

---

## 🧩 下一步

- 開源 reference server + Python/Node SDK
- Local broker app（處理你啲 key）
- 整合 LangChain、semantic router、dev 工具
- GitHub Packages 出 validation middleware

---

## 🧠 作者係邊位？

呢個協議（Agent-Native Challenge Protocol）由：

**Wai Yip, WONG** 設計、構思、實做、講晒事

🔗 [LinkedIn](https://www.linkedin.com/in/wai-yip-wong/)  
💻 [GitHub](https://waiyip000.github.io/)

---

## 📄 License

用改咗嘅 MIT License，包埋 Reasoning Attribution。詳情睇 `LICENSE`。
