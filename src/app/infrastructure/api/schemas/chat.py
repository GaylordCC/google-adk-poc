"""HTTP contracts (Pydantic) for the chat endpoint.

GUIDE: these are transport-only shapes — never reuse domain entities
(domain/models/) or application DTOs (application/dtos.py) here
directly, even when they look identical today. The API's public
contract should be free to evolve independently from internal shapes.
"""
from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    reply: str
