"""Data Transfer Objects for application use cases with richer inputs/outputs.

GUIDE: SendMessageUseCase (use_cases/send_message.py) is simple enough to
take primitives directly (see domain/ports/inbound.py) and doesn't need
these yet. Reach for a DTO here once a use case needs multiple fields or
a structured result.

Keep these separate from infrastructure/api/schemas/ (HTTP contracts) and
from domain/models/ (business entities) — three different reasons to
change, three different shapes, even when they look identical today.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class SendMessageInput:
    """GUIDE: example shape for a future, richer use case. Unused for now."""

    session_id: str
    content: str


@dataclass(frozen=True)
class SendMessageOutput:
    """GUIDE: example shape for a future, richer use case. Unused for now."""

    reply_text: str
