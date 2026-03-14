# 🤖 RagChat — AI Chatbot with RAG

> A full-stack AI chatbot powered by **Groq (Llama 3.3 70B)** with file upload Q&A, persistent memory, and a beautiful dark neon UI with sidebar.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-F55036?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 Table of Contents

- [Features](#-features)
- [Preview](#-preview)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Author](#-author)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💬 Multi-turn Chat | Remembers full conversation history |
| 📄 File Q&A | Upload PDF, TXT, DOCX and ask questions |
| 🧠 Personal Memory | Always knows who you are via `memory.json` |
| 💾 Persistent History | All conversations saved to JSON files |
| 🗂️ Recent Chats | Switch between saved conversations in sidebar |
| 🎨 Dark Neon UI | Beautiful blue neon interface with sidebar |
| ⚡ Free & Fast | Powered by Groq free tier (14,400 req/day) |
| 🔄 Session Management | Create, switch, and delete conversations |

---

## 🖥️ Preview

```
╔══════════════════════════════════════════════════════════════╗
║  🤖 Haider AI        │  Haider Assistant                     ║
║                      │                                        ║
║  + New conversation  │  ┌─────────────────────────────────┐   ║
║                      │  │ AI: Hello! I am Haider           │  ║
║  RECENT CHATS        │  │     Assistant. Ask me anything.  │  ║
║  ▶ What is Python?   │  └─────────────────────────────────┘  ║
║  ▶ Explain FastAPI   │                                       ║
║                      │         ┌──────────────────┐          ║
║                      │         │ You: Hello!      │          ║
║                      │         └──────────────────┘          ║
║                      │  ┌─────────────────────────────────┐  ║
║                      │  │ AI: Hello! How can I help you?  │  ║
║                      │  └─────────────────────────────────┘  ║
║                      │                                        ║
║  Haider AI           │  [ 📄 ] [ Message Haider AI...  ] [▶] ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🗂️ Project Structure

```
ragchat/
├── 📄 main.py              # FastAPI routes & endpoints
├── ⚙️  config.py            # Settings, API key, system prompt
├── 📐 models.py            # Pydantic data models
├── 🤖 chat_service.py      # Groq AI integration
├── 💾 history_store.py     # Chat history management
├── 📁 file_handler.py      # PDF, TXT, DOCX text extraction
├── 🧠 memory.json          # Personal memory about the user
├── 🎨 chatbot_ui.html      # Frontend dark neon UI
├── 🔒 .env                 # API keys (never commit!)
├── 📋 .env.example         # Template for environment variables
├── 📦 requirements.txt     # Python dependencies
└── 💬 chat_histories/      # Saved conversations (auto-created)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Free Groq API key → [console.groq.com](https://console.groq.com)

### 1. Clone the repository

```bash
git clone https://github.com/HaiderNeuralNet/Ragchat-Haider.git
cd Ragchat-Haider
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=gsk_your_key_here
SYSTEM_PROMPT=You are a helpful assistant.
```

> Get your free API key at: **https://console.groq.com**

### 4. Configure personal memory (optional)

Edit `memory.json` to personalize the AI:

```json
{
  "name": "Haider",
  "profession": "Software Developer",
  "location": "Pakistan",
  "interests": ["AI", "chatbots", "modern UI"],
  "current_project": "AI Chatbot with FastAPI and Groq"
}
```

### 5. Run the app

```bash
python -m uvicorn main:app --port 8000
```

### 6. Open in browser

```
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve the chat UI |
| `POST` | `/chat` | Send a message |
| `POST` | `/chat/stream` | Streaming chat response |
| `POST` | `/upload` | Upload a file (PDF/TXT/DOCX) |
| `GET` | `/history/{session_id}` | Get chat history |
| `DELETE` | `/history/{session_id}` | Clear chat history |
| `GET` | `/sessions` | Get all saved sessions |
| `GET` | `/health` | Health check |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Python, FastAPI | REST API server |
| **AI Model** | Groq — Llama 3.3 70B | AI responses (free) |
| **Frontend** | HTML, CSS, JavaScript | Chat UI |
| **File Parsing** | PyPDF2, python-docx | Extract text from files |
| **Storage** | JSON files | Save chat history |
| **Server** | Uvicorn | ASGI web server |

---

## 📦 Requirements

```
fastapi
uvicorn[standard]
groq
python-dotenv
sse-starlette
python-multipart
PyPDF2
python-docx
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 💡 How It Works

### Chat Flow
```
User types message
        ↓
FastAPI receives request  (main.py)
        ↓
Load full conversation history  (history_store.py)
        ↓
Send history + system prompt to Groq  (chat_service.py)
        ↓
Groq (Llama 3.3 70B) generates reply
        ↓
Save reply to JSON file  (history_store.py)
        ↓
Display reply in browser  (chatbot_ui.html)
```

### File Q&A Flow
```
User uploads PDF / TXT / DOCX
        ↓
Extract all text  (file_handler.py)
        ↓
Inject text into chat history as context
        ↓
User asks questions → AI answers based on file
```

### Why Multi-turn Memory Works
```
Every request includes FULL conversation history:

Turn 1: [user: "hi"]
Turn 2: [user: "hi", ai: "hello!", user: "what is Python?"]
Turn 3: [user: "hi", ai: "hello!", ..., user: "give an example"]

AI always sees everything → remembers context perfectly ✅
```

---

## 🔒 Security

- ✅ Use `.env.example` to share required variables
- ✅ Regenerate your API key if accidentally exposed
- ✅ File uploads are processed and deleted immediately

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

---

## 👤 Author

**Haider**

- 🐙 GitHub: [@HaiderNeuralNet](https://github.com/HaiderNeuralNet)
- 💼 Project: [Ragchat-Haider](https://github.com/HaiderNeuralNet/Ragchat-Haider)

---

## ⭐ Support

If you found this project helpful, please give it a **⭐ star** on GitHub!

It helps others discover the project and motivates continued development. 🚀

---

*Built with ❤️ by Haider — learning AI by building real projects*
