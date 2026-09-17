"""Centralized application settings.

GUIDE: every configurable value (API keys, model name, environment) must
come through this Settings object — never scatter os.getenv() calls
around the codebase. Values are read from `.env` automatically.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    environment: str = "local"
    # GUIDE: add Google ADK configuration here once credentials are set
    # up in .env, e.g.:
    #   google_api_key: str
    #   agent_model: str = "gemini-2.0-flash"


settings = Settings()
