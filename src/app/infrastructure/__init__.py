"""Infrastructure layer: everything that talks to the outside world.

GUIDE: this is the ONLY layer allowed to import fastapi, google.adk,
sqlalchemy, httpx, etc. It implements the ports declared under
domain/ports/ and exposes them either as driving adapters (api/) or
driven adapters (adapters/, persistence/, clients/).
"""
