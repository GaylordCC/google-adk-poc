"""Domain-level exceptions.

GUIDE: these describe business-meaningful failures, not HTTP failures.
Never raise fastapi.HTTPException from domain/ or application/ — the
translation to an HTTP status code happens in exactly one place:
infrastructure/api/error_handlers.py.
"""


class DomainError(Exception):
    """Base class for every exception raised by the domain layer."""


class InvalidMessageError(DomainError):
    """GUIDE: raised by conversation_policy.validate_message_content()
    when a message violates a business rule."""


class AgentUnavailableError(DomainError):
    """GUIDE: raised by an AgentPort implementation (e.g. the Google ADK
    adapter) when the underlying agent engine fails, times out, or
    returns an error — the domain sees this generic error, never a
    google.adk-specific exception type."""
