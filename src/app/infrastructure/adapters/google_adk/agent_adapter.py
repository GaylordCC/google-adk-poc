"""Concrete AgentPort implementation backed by Google ADK.

GUIDE: this class is the ONLY bridge between the domain's AgentPort
contract (domain/ports/outbound.py) and the real google.adk Runner built
in agent_factory.py. Its job:
  1. receive a domain Message
  2. call the ADK runner
  3. map the ADK result into a domain AgentReply via mappers.py
  4. translate any ADK-specific error into a domain
     AgentUnavailableError (domain/exceptions.py)

Left unimplemented on purpose — no agent logic yet, just the seam where
the real integration will plug in.
"""
from app.domain.models.conversation import AgentReply, Message
from app.domain.ports.outbound import AgentPort


class GoogleAdkAgentAdapter(AgentPort):
    def __init__(self, runner) -> None:
        # GUIDE: `runner` is whatever agent_factory.build_google_adk_agent()
        # returns — kept untyped here on purpose until that function exists.
        self._runner = runner

    async def ask(self, session_id: str, message: Message) -> AgentReply:
        raise NotImplementedError
