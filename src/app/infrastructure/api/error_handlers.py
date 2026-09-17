"""Maps domain exceptions to HTTP responses.

GUIDE: this is the ONLY place a domain exception should be translated
into an HTTP status code — routers must never do this translation
inline, and domain/application must never raise fastapi.HTTPException.
"""
from fastapi import Request
from fastapi.responses import JSONResponse

from app.domain.exceptions import DomainError


async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
    # GUIDE: refine this into per-exception-type status codes as real
    # domain exceptions get raised (e.g. InvalidMessageError -> 422,
    # AgentUnavailableError -> 503). A flat 400 is a placeholder.
    return JSONResponse(status_code=400, content={"detail": str(exc)})
