"""Use case: send a message within a conversation and get the agent's reply.

GUIDE: this class depends only on AgentPort (a domain contract, see
domain/ports/outbound.py) — never on a concrete adapter. The concrete
AgentPort implementation is chosen and injected from
infrastructure/api/deps.py (the composition root). No google.adk logic
belongs here, only orchestration of domain concepts.

This implements the app.domain.ports.inbound.SendMessageUseCase contract.
"""
from app.domain.ports.outbound import AgentPort


class SendMessageUseCase:
    def __init__(self, agent: AgentPort) -> None:
        self._agent = agent

    async def execute(self, session_id: str, content: str) -> str:
        # GUIDE: real orchestration goes here in a later iteration:
        #   1. validate `content` via domain.services.conversation_policy
        #   2. build a domain Message
        #   3. call self._agent.ask(session_id, message)
        #   4. return reply.text
        # Left unimplemented on purpose — no agent logic yet, just the
        # architectural seam where it will plug in.
        raise NotImplementedError
