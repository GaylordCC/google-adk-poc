"""Liveness/readiness endpoints.

GUIDE: /health answers "is the process alive". /health/ready answers
"can it actually serve traffic" — once there are real dependencies to
check (e.g. Google ADK credentials, a database), verify them here. No
business or agent logic belongs in this file.
"""
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}


@router.get("/health/ready")
async def readiness_check() -> dict:
    # GUIDE: add real dependency checks here later, e.g. verifying
    # Google ADK credentials are configured before reporting "ready".
    return {"status": "ready"}
