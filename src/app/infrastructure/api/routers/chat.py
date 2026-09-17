"""Driving adapter: translates HTTP <-> SendMessageUseCase.

GUIDE: no business logic belongs in this file — only request parsing,
delegating to the use case (resolved via deps.py), and shaping the HTTP
response. Calling this endpoint today raises NotImplementedError, since
neither the use case's orchestration nor the Google ADK adapter behind
it are implemented yet (this pass is architecture only).
"""
from fastapi import APIRouter, Depends

from app.infrastructure.api.deps import get_send_message_use_case
from app.infrastructure.api.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def send_chat_message(
    payload: ChatRequest,
    use_case=Depends(get_send_message_use_case),
) -> ChatResponse:
    reply_text = await use_case.execute(payload.session_id, payload.message)
    return ChatResponse(reply=reply_text)
