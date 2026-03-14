from __future__ import annotations
from typing import AsyncGenerator
from groq import Groq
from config import GROQ_API_KEY, SYSTEM_PROMPT, MODEL, MAX_TOKENS
from history_store import append_message

client = Groq(api_key=GROQ_API_KEY)


def get_reply(session_id: str, user_message: str, system_prompt: str | None = None) -> str:
    messages = append_message(session_id, "user", user_message)

    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": system_prompt or SYSTEM_PROMPT},
            *messages
        ]
    )

    reply = response.choices[0].message.content
    append_message(session_id, "assistant", reply)
    return reply


async def stream_reply(
    session_id: str,
    user_message: str,
    system_prompt: str | None = None,
) -> AsyncGenerator[str, None]:
    messages = append_message(session_id, "user", user_message)

    full_reply = ""

    stream = client.chat.completions.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": system_prompt or SYSTEM_PROMPT},
            *messages
        ],
        stream=True
    )

    for chunk in stream:
        text = chunk.choices[0].delta.content or ""
        full_reply += text
        yield text

    append_message(session_id, "assistant", full_reply)