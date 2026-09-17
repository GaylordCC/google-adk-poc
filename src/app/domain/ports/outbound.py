"""Outbound ports: contracts the domain/application NEEDS from the
outside world. Concrete implementations (adapters) live under
infrastructure/adapters/ and infrastructure/persistence/.

GUIDE: nothing in this file may import fastapi, google.adk, sqlalchemy,
etc. — only typing.Protocol and domain types.
"""
from typing import Protocol

from app.domain.models.conversation import AgentReply, Message


class AgentPort(Protocol):
    """Contract any conversational-agent engine must satisfy.

    GUIDE: today this will be implemented by a Google ADK adapter
    (infrastructure/adapters/google_adk/agent_adapter.py). Tomorrow it
    could be a different framework, or a fake used in tests — the domain
    never knows which, and never imports google.adk to find out.
    """

    async def ask(self, session_id: str, message: Message) -> AgentReply: ...


class ConversationRepositoryPort(Protocol):
    """Contract for persisting/retrieving conversation history.

    GUIDE: implement this later under infrastructure/persistence/ once
    the project needs to remember past messages (e.g. an in-memory repo
    first, a real database later — same port, different adapter).
    """

    async def save(self, session_id: str, message: Message) -> None: ...
