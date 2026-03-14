import os
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from models import ChatRequest, ChatResponse, UploadResponse
from chat_service import get_reply, stream_reply
from history_store import load_history, clear_history
from file_handler import extract_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def serve_ui():
    return FileResponse(os.path.join(BASE_DIR, "chatbot_ui.html"))

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    try:
        reply = get_reply(req.session_id, req.message, req.system_prompt)
        return ChatResponse(session_id=req.session_id, reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload", response_model=UploadResponse)
async def upload_file(
    session_id: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # Save file temporarily
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        # Extract text
        text = extract_text(file_path, file.filename)

        if not text.strip():
            raise ValueError("Could not extract text from file.")

        # Trim to avoid token limits (keep first 12000 chars)
        trimmed = text[:12000]
        if len(text) > 12000:
            trimmed += "\n\n[File trimmed due to length...]"

        # Inject file content into chat history as context
        context_msg = (
            f"The user uploaded a file called '{file.filename}'. "
            f"Here is its content:\n\n{trimmed}\n\n"
            f"Answer the user's questions based on this file."
        )

        from history_store import append_message
        append_message(session_id, "user", context_msg)
        append_message(session_id, "assistant", 
            f"I've read '{file.filename}' ({len(text):,} characters). Ask me anything about it!")

        # Cleanup temp file
        os.remove(file_path)

        return UploadResponse(
            session_id=session_id,
            filename=file.filename,
            characters=len(text),
            message=f"File '{file.filename}' uploaded successfully!"
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/history/{session_id}")
def get_history(session_id: str):
    return {"session_id": session_id, "messages": load_history(session_id)}

@app.delete("/history/{session_id}")
def delete_history(session_id: str):
    clear_history(session_id)
    return {"message": f"History cleared for session {session_id}"}

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/health")
def health():
    return {"status": "ok"}

# ← ADD HERE ↓
@app.get("/sessions")
def get_sessions():
    sessions = []
    history_dir = os.path.join(BASE_DIR, "chat_histories")

    if not os.path.exists(history_dir):
        return {"sessions": []}

    for filename in os.listdir(history_dir):
        if filename.endswith(".json"):
            session_id = filename.replace(".json", "")
            history = load_history(session_id)

            title = "New conversation"
            for msg in history:
                if msg["role"] == "user" and len(msg["content"]) < 200:
                    title = msg["content"][:40]
                    if len(msg["content"]) > 40:
                        title += "..."
                    break

            if len(history) > 0:
                sessions.append({
                    "session_id": session_id,
                    "title": title,
                    "count": len(history)
                })

    sessions.sort(key=lambda x: x["session_id"], reverse=True)
    return {"sessions": sessions}