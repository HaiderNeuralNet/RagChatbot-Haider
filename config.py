from dotenv import load_dotenv
import os
import json

load_dotenv()

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY environment variable is not set")

# Load personal memory
MEMORY_PATH = os.path.join(os.path.dirname(__file__), "memory.json")
if os.path.exists(MEMORY_PATH):
    with open(MEMORY_PATH, "r") as f:
        memory = json.load(f)
    MEMORY_TEXT = "\n".join([f"- {k}: {v}" for k, v in memory.items()])
else:
    MEMORY_TEXT = ""

SYSTEM_PROMPT: str = f"""You are Haider Assistant, a personal AI.

Here is what you know about the user:
{MEMORY_TEXT}

Always use this information when answering questions about the user.
Be helpful, modern, and concise."""

MODEL: str = "llama-3.3-70b-versatile"
MAX_TOKENS: int = 1024