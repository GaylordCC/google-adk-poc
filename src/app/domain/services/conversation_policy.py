"""Pure business rules about conversations — no I/O, no framework imports.

GUIDE: this is where rules that span more than a single entity live (e.g.
"reject a message longer than N characters", "close a conversation after
X turns"). Every function here should be synchronous and side-effect
free, which is exactly what makes domain logic trivial to unit test.

Left unimplemented on purpose in this scaffolding pass — no agent logic
yet, just the seam where real validation rules will plug in.
"""


def validate_message_content(content: str) -> None:
    """GUIDE: raise app.domain.exceptions.InvalidMessageError when a rule
    is violated (e.g. empty content, exceeds max length)."""
    raise NotImplementedError
