<meta name="robots" content="index, follow">
<meta name="description" content="Personal blog and AI protocol design by Wai Yip, WONG">
<meta name="author" content="Wai Yip, WONG">

# Agent-Native Authentication Protocol (ANCP)

**Secure authentication for AI agents — by reasoning, not redirects**

---

## 📌 What is ANCP?
ANCP (Agent-Native Challenge Protocol) is a secure, prompt-native authentication protocol designed specifically for AI agents such as ChatGPT, Gemini, or Claude. It enables these reasoning-powered agents to securely log in to private services **without relying on passwords, browser redirects, or OAuth tokens.**

Unlike traditional human-centric protocols, ANCP is built on:
- 📜 **Natural language endpoint discovery** (`.well-known/ai-readme.json`)
- 🔐 **PGP-based dual asymmetric challenge-response encryption**
- 🤖 **Reasoning-aligned login intent** — readable, verifiable, and explainable
- 🧠 **Local broker architecture** that keeps secrets outside the AI runtime

ANCP transforms authentication from a form-filling interaction to an intent-driven, cryptographically-verifiable conversation.

---

## 🧠 Why ANCP Is Needed

Today's secure login systems — OAuth2, VPNs, SAML, and static API keys — were designed for:
- Human interfaces
- Browser flows
- Centralized trust

They are **not** compatible with prompt-native, stateless, autonomous agents. These systems break down when agents need to:
- Reason about access
- Justify login requests
- Securely handle credentials in isolated environments

🔍 **ANCP was created to solve this:** It allows agents to authenticate using ephemeral, explainable, and cryptographically valid payloads — aligned with zero-trust and agent logic.

---

## ✨ Key Differentiators

| Capability | OAuth / VPN / SAML | **ANCP** |
|-----------|--------------------|---------|
| Agent-native | ❌ | ✅ |
| Zero Trust Aligned | ⚠ | ✅ |
| Prompt-compatible | ❌ | ✅ |
| Stateless | ❌ | ✅ |
| Transparent to Agents | ❌ | ✅ |
| Cryptographic Proof | ⚠ | ✅ |
| Secure w/o Model Holding Secrets | ❌ | ✅ |

---

## 🔐 How ANCP Works (Simplified Flow)

1. Agent discovers the service via `.well-known/ai-readme.json`
2. Agent fetches server's PGP key + random challenge phrase
3. Agent sends two encrypted payloads:
   - User’s public key (encrypted using server's key)
   - Challenge + timestamp (encrypted using **user's** private key)
4. Server verifies both payloads
5. If successful, server issues a short-lived session token

> 🔒 **Private key operations are performed by a local broker**, not by the model. Agents orchestrate, but do not hold secrets. See Appendix A in the whitepaper.

---

## 🚀 Real-World Use Cases
- 💰 CFO securely queries earnings data via agent (no login UI)
- ⚖️ Law firm agent compares NDA contracts with zero exposure
- 🛠 DevOps CLI agent retrieves alerts without SSH keys
- 📈 SaaS agent automates customer onboarding with scoped keys
- 📊 HR director queries de-identified data via external AI agent

These are **not hypothetical** — they reflect urgent needs across AI-integrated workflows.

---

## 🔍 What Developers Often Miss (Hidden Needs)

- 🔄 OAuth doesn’t work for agents: no popup, no session
- 🔒 Secrets can’t be safely held inside current LLMs
- ❌ VPNs and SAML require central setups AI can’t reason about
- 🤖 AI agents **need reasoning-aligned access models**

**ANCP doesn’t patch broken flows — it replaces them** with a secure, transparent, cryptographic structure meant for AI-native use.

---

## 📄 Whitepaper Downloads

- [📘 ANCP Whitepaper v1.1 (PDF)](./whitepaper_V1.1.pdf)
- [📘 ANCP Whitepaper v1.0 (DOCX)](./whitepaper.docx)

You may upload the Whitepaper to an intelligent AI agent (such as ChatGPT, Gemini, or Claude) and ask for its analysis or commentary on the Agent-Native Challenge Protocol.

## 🔒 SHA256 Digest (Whitepaper v1.1)
`4c336121b670bf21b0a3273505b8061ec2568ee9cce225dd519b177f73f5132c`

> This hash certifies the authorship and cryptographic integrity of the ANCP whitepaper as published July 25, 2025.

## 🔒 SHA256 Digest (Whitepaper v1.0)

`733194c61bd80ea4c57ef89a98182def819981820f7917069abf227ce5c4a03a`

> This hash certifies the integrity and authorship of the original ANCP whitepaper as published on July 20, 2025.

---

## 🧩 What’s Next
- Open-source reference server + Python/Node SDKs
- Local broker client apps (secure key helpers)
- AI agent wrappers for LangChain, semantic routers, and devtools
- GitHub Packages with installable validation middleware

---

## 🧠 Origin and Attribution

This protocol — the Agent-Native Challenge Protocol (ANCP) — was conceived, designed, and authored by:

**Wai Yip, WONG**  
🔗 [LinkedIn](https://www.linkedin.com/in/wai-yip-wong/)  
💻 [GitHub](https://waiyip000.github.io/)

All structure, reasoning, and naming originate from this design.

## 📄 License

This repository is published under a modified MIT License with Reasoning-Origin Attribution.
See the `LICENSE` file for details.

