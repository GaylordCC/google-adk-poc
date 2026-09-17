"""Domain layer.

GUIDE: this is the core of the hexagonal architecture. Nothing here may
import fastapi, google.adk, sqlalchemy or any other framework/library —
only plain Python (dataclasses, typing.Protocol, stdlib). If you feel the
need to import something from `infrastructure` here, that logic belongs
in a different layer.
"""
