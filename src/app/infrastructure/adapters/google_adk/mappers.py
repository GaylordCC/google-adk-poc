"""Translation between google.adk types and domain types.

GUIDE: keep every google.adk-specific type confined to this module (plus
agent_adapter.py). Nothing outside infrastructure/adapters/google_adk/
should ever see a raw ADK object — domain/models/conversation.py defines
the only shapes the rest of the app is allowed to depend on.

Left unimplemented on purpose — no agent logic yet.
"""
