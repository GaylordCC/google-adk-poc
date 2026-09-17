"""Shared pytest fixtures.

GUIDE: fixtures that many tests need (a FastAPI TestClient, fakes for
ports like AgentPort) live here. Keep fixtures for a single test file
local to that file instead.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
