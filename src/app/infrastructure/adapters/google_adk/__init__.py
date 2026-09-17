"""Google ADK adapter package.

GUIDE: this package is the ONLY place in the project allowed to import
`google.adk`. It implements AgentPort (domain/ports/outbound.py) so the
rest of the application never talks to the ADK SDK directly.

No agent logic is implemented yet — this scaffolding pass only lays out
where each responsibility will live. See agent_factory.py,
agent_adapter.py, mappers.py and tools/ below.
"""
