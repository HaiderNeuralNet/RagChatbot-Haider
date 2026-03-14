from __future__ import annotations
import json
import os

HISTORY_DIR = "chat_histories"
os.makedirs(HISTORY_DIR, exist_ok=True)


def _path(session_id: str) -> str:
    return os.path.join(HISTORY_DIR, f"{session_id}.json")


def load_history(session_id: str) -> list[dict]:
    path = _path(session_id)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


def save_history(session_id: str, messages: list[dict]) -> None:
    with open(_path(session_id), "w") as f:
        json.dump(messages, f, indent=2)


def append_message(session_id: str, role: str, content: str) -> list[dict]:
    history = load_history(session_id)
    history.append({"role": role, "content": content})
    save_history(session_id, history)
    return history


def clear_history(session_id: str) -> None:
    path = _path(session_id)
    if os.path.exists(path):
        os.remove(path)


def list_sessions() -> list[dict]:
    sessions = []
    if not os.path.exists(HISTORY_DIR):
        return []
    for filename in os.listdir(HISTORY_DIR):
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
    return sorted(sessions, key=lambda x: x["session_id"], reverse=True)