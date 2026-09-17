"""Inbound ports: use cases the application layer OFFERS to driving
adapters (e.g. infrastructure/api/routers/chat.py).

GUIDE: keep these signatures expressed in primitives or domain types
only — never import anything from `application` or `infrastructure`
here. The dependency direction is: infrastructure -> application ->
domain. Domain must never depend on an outer layer.
"""
from typing import Protocol


class SendMessageUseCase(Protocol):
    """GUIDE: implemented by application/use_cases/send_message.py.
    A driving adapter (e.g. a FastAPI router) depends on THIS contract,
    never on the concrete class — that keeps the API layer swappable too."""

    async def execute(self, session_id: str, content: str) -> str: ...
