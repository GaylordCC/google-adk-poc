"""Composition root: builds the FastAPI application.

GUIDE: this is the only module that assembles routers + exception
handlers into a running app. It must never contain business logic
itself — only wiring.

Run with (from the project root):
    PYTHONPATH=src venv/bin/uvicorn app.main:app --reload
"""
from fastapi import FastAPI

from app.domain.exceptions import DomainError
from app.infrastructure.api.error_handlers import domain_error_handler
from app.infrastructure.api.routers import chat, health

app = FastAPI(title="google-adk-poc")

app.include_router(health.router)
app.include_router(chat.router)

app.add_exception_handler(DomainError, domain_error_handler)
