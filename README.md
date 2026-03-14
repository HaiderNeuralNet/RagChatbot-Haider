# 🤖 RagChat — AI Chatbot with RAG

A full-stack AI chatbot powered by **Groq (Llama 3.3 70B)** with file upload, YouTube video Q&A, persistent memory, and a beautiful dark neon UI.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- 💬 **Multi-turn conversation** — remembers full chat history
- 📄 **File upload Q&A** — upload PDF, TXT, DOCX and ask questions
- 🎥 **YouTube video Q&A** — paste a YouTube link and ask questions about it
- 🧠 **Personal memory** — always knows who you are via `memory.json`
- 💾 **Persistent chat history** — all conversations saved to JSON files
- 🗂️ **Recent chats sidebar** — switch between saved conversations
- 🎨 **Dark neon UI** — beautiful blue neon interface with sidebar
- ⚡ **Free & Fast** — powered by Groq's free tier (14,400 req/day)

---

## 📸 Preview

```
┌─────────────────────────────────────────────────────┐
│  Haider AI          │  Haider Assistant              │
│  + New conversation │                                │
│                     │  AI: Hello! Ask me anything.   │
│  RECENT CHATS       │                                │
│  > Current session  │  You: What is Python?          │
│  > Old chat 1       │                                │
│  > Old chat 2       │  AI: Python is a programming.. │
│                     │                                │
│                     │  [📄] [🎥] [Message...] [Send] │
└─────────────────────────────────────────────────────┘
```

---

## 🗂️ Project Structure

```
ragchat/
├── main.py              # FastAPI routes & endpoints
├── config.py            # Settings, API key, system prompt
├── models.py            # Pydantic data models
├── chat_service.py      # Groq AI integration
├── history_store.py     # Chat history management
├── file_handler.py      # PDF, TXT, DOCX text extraction
├── video_handler.py     # YouTube transcript fetcher
├── memory.json          # Personal memory about the user
├── chatbot_ui.html      # Frontend dark neon UI
├── .env                 # API keys 
├── .env.example         # Template for environment variables
├── requirements.txt     # Python dependencies
└── chat_histories/      # Saved conversations (auto-created)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/HaiderNeuralNet/RagChatbot-Haider.git
cd RagChatbot-Haider 
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```env
GROQ_API_KEY=gsk_your_key_here
SYSTEM_PROMPT=You are a helpful assistant.
```

Get a free Groq API key at: **https://console.groq.com**

### 4. Update personal memory 

Edit `memory.json` to tell the AI who you are:

```json
{
  "name": "Your Name",
  "profession": "Software Developer",
  "location": "Your City",
  "interests": ["AI", "coding"],
  "current_project": "AI Chatbot"
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
| `GET` | `/` | Serve chat UI |
| `POST` | `/chat` | Send a message |
| `POST` | `/chat/stream` | Streaming chat |
| `POST` | `/upload` | Upload a file (PDF/TXT/DOCX) |
| `POST` | `/video` | Load YouTube video transcript |
| `GET` | `/history/{session_id}` | Get chat history |
| `DELETE` | `/history/{session_id}` | Clear chat history |
| `GET` | `/sessions` | Get all saved sessions |
| `GET` | `/health` | Health check |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, FastAPI |
| **AI Model** | Groq — Llama 3.3 70B (free) |
| **Frontend** | HTML, CSS, JavaScript |
| **File Parsing** | PyPDF2, python-docx |
| **Video** | youtube-transcript-api |
| **Storage** | JSON files |
| **Server** | Uvicorn |

---

## 📦 Requirements

```txt
fastapi
uvicorn[standard]
groq
python-dotenv
sse-starlette
python-multipart
PyPDF2
python-docx
youtube-transcript-api
```

---

## 💡 How It Works

```
User sends message
      ↓
FastAPI receives request (main.py)
      ↓
Load full chat history (history_store.py)
      ↓
Send history + system prompt to Groq API (chat_service.py)
      ↓
Groq returns AI reply
      ↓
Save reply to JSON file (history_store.py)
      ↓
Return reply to browser (chatbot_ui.html)
```

### File/Video Q&A Flow

```
User uploads file / pastes YouTube URL
      ↓
Extract text (file_handler.py / video_handler.py)
      ↓
Inject text into chat history as context
      ↓
User asks questions → AI answers based on content
```

---

## 🔒 Security

- Never commit your `.env` file
- `.gitignore` is configured to exclude `.env`
- Regenerate your API key if accidentally exposed
- Use `.env.example` to share required variables

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Haider**
- GitHub: [@HaiderNeuralNet](https://github.com/HaiderNeuralNet)

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
