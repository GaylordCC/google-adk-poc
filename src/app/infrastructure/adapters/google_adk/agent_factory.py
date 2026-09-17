"""Builds and configures the Google ADK Agent/Runner.

GUIDE: this module will read `app.config.settings` (model name, GCP
project/credentials, system instructions, registered tools) and build a
ready-to-use ADK Agent/Runner exactly once (or once per process) — not
on every request. `agent_adapter.py` then wraps that object behind
AgentPort.

Left unimplemented on purpose: no google.adk import, no agent
construction yet. This is a placeholder for the next iteration, once
credentials exist in .env.
"""


def build_google_adk_agent():
    raise NotImplementedError
