from __future__ import annotations
from pydantic import BaseModel
from typing import Literal

class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    session_id: str
    message: str
    system_prompt: str | None = None

class ChatResponse(BaseModel):
    session_id: str
    reply: str

class UploadResponse(BaseModel):
    session_id: str
    filename: str
    characters: int
    message: str