"""Core business entities for the conversation flow.

GUIDE: these are plain, framework-free objects — the vocabulary the whole
application speaks internally. Adapters (FastAPI schemas, Google ADK
objects, ORM models) all translate into/out of these shapes; these
shapes never travel outward as-is.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    """A single message sent by a user within a conversation session.

    GUIDE: add real invariants here as they emerge (e.g. max length, no
    empty content) inside a __post_init__ that raises a domain exception
    (see domain/exceptions.py). No agent logic belongs here — just the
    shape and rules of "what a valid message is".
    """

    content: str


@dataclass(frozen=True)
class AgentReply:
    """The reply produced by whatever agent implementation answers a Message.

    GUIDE: this is the domain's OWN shape for a reply. A Google ADK
    response object must be mapped into this by an adapter
    (infrastructure/adapters/google_adk/mappers.py) — it should never
    reach this far as-is.
    """

    text: str
