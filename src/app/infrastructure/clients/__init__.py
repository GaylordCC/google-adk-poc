"""HTTP clients to external services (other than Google ADK itself, which
has its own adapter package under infrastructure/adapters/google_adk/).

GUIDE: add one module per external service here as the project needs to
call out to something (e.g. weather_client.py, payments_client.py). Each
client should be wrapped behind a port so use cases don't depend on the
concrete HTTP library used.
"""
