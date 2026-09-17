"""Composition: wires concrete adapters into application use cases.

GUIDE: this is the ONLY place that should know which concrete AgentPort
implementation is active for a given environment. Swapping Google ADK
for something else later — or wiring a fake for tests — means changing
only this file, never the routers or the use case itself.
"""
from app.application.use_cases.send_message import SendMessageUseCase


def get_send_message_use_case() -> SendMessageUseCase:
    # GUIDE: no concrete AgentPort implementation is wired in yet (see
    # infrastructure/adapters/google_adk/), so this raises on purpose.
    # Once agent_factory.py / agent_adapter.py exist, this becomes:
    #   agent = build_google_adk_agent(settings)
    #   return SendMessageUseCase(agent=agent)
    raise NotImplementedError
