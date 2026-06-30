# 🏦 SBI AssistAI

![Hackathon](https://img.shields.io/badge/Hackathon-SBI%20GFF%202026-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Python-green)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

### Banking Made Simple for Everyone

SBI AssistAI is a **multilingual banking assistant prototype** built using **FastAPI**. It helps users access common SBI banking services, receive multilingual banking guidance, detect banking frauds, and continue conversations using contextual follow-up support.

Developed as part of **SBI Hackathon @ GFF 2026**.

---

# 📌 Problem Statement

Millions of banking customers struggle with digital banking due to:

- 🌐 Language barriers
- 📱 Complex banking interfaces
- 👴 Limited digital literacy among senior citizens
- 🌾 Financial inclusion challenges in rural areas
- ⚠️ Increasing online banking frauds

SBI AssistAI aims to simplify banking by providing accessible, multilingual, and intelligent banking assistance.

---

# ✨ Features

- 🌍 Multilingual Banking Support (English, Kannada & Hindi)
- 💬 Context-Aware Follow-up Conversations
- 🏦 Banking Guidance for Common SBI Services
- 🔐 Fraud Detection & Fraud Awareness
- 🚨 Multi-Threat Fraud Detection
- 🌐 Automatic Language Detection
- 📖 Rule-Based Banking Knowledge Base
- ⚡ FastAPI REST API
- 📚 Interactive Swagger Documentation

---

# 🛠️ Technology Stack

### Backend
- Python
- FastAPI

### Banking Intelligence
- Rule-Based Banking Engine
- Keyword Matching
- Conversation Memory
- Dynamic Follow-up Engine

### Language Processing
- langdetect

### API Documentation
- Swagger UI (OpenAPI)

### Version Control
- Git
- GitHub

### Future Technologies
- Large Language Models (LLMs)
- Speech-to-Text
- Text-to-Speech
- Microsoft Azure

---

# 📂 Project Structure

```text
sbi-assist-ai/
│
├── architecture/
├── demo/
├── docs/
├── prototype/
└── src/
    ├── app.py
    ├── knowledge_base.py
    ├── fraud_module.py
    ├── requirements.txt
    └── README.md
```

---

# 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/tvshetty-x/sbi-assist-ai.git
```

### Navigate to the Source Folder

```bash
cd sbi-assist-ai/src
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the FastAPI Server

```bash
uvicorn app:app --reload
```

### Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

| Endpoint | Description |
|-----------|-------------|
| `/` | Welcome endpoint |
| `/health` | API health check |
| `/ask` | Banking Assistant |
| `/follow-up` | Context-Aware Follow-up |
| `/fraud-check` | Fraud Detection |
| `/detect-language` | Detect Language |
| `/multilingual-help` | Multilingual Help |
| `/banking-help` | Banking Services |

---

# 💡 How SBI AssistAI Works

```text
User Question
        │
        ▼
Language Detection
        │
        ▼
Banking Intent Detection
        │
        ▼
Knowledge Base Lookup
        │
        ▼
Conversation Memory
        │
        ▼
Response Generation
```

---

# 🛡️ Fraud Detection

The fraud detection module identifies common banking frauds including:

- OTP Scam
- PIN Theft
- Phishing
- Fake Customer Care
- Fake KYC
- UPI Scam
- ATM Skimming

The assistant supports **multi-threat fraud detection**, allowing multiple fraud indicators to be identified from a single message while calculating an **overall risk level**.

---

# 🌍 Multilingual Support

Currently supported languages:

- 🇬🇧 English
- 🇮🇳 Kannada
- 🇮🇳 Hindi

The assistant also supports several **transliterated inputs**, such as:

```text
nange password reset madbeku
```

making banking assistance more accessible to users who type regional languages using the English keyboard.

---

# 🔮 Future Scope

- 🤖 AI-powered intent detection using Large Language Models (LLMs)
- 🎤 Voice-based interaction (Speech-to-Text & Text-to-Speech)
- 👤 Session-based conversation memory
- ☁️ Microsoft Azure cloud deployment
- 🗄️ PostgreSQL integration
- 🏦 Integration with SBI digital banking ecosystem
- 📱 Mobile application support

---

# 👩‍💻 Developer

**Thvishaa Shetty**

Engineering Student

Built for **SBI Hackathon @ GFF 2026**

---

# 🙏 Acknowledgement

SBI AssistAI was developed as a hackathon prototype to demonstrate how multilingual conversational banking assistance can improve digital banking accessibility, fraud awareness, and financial inclusion.
