"""Chat history endpoints supporting the LearningStyleChat component."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.jwt_handler import get_current_user
from backend.database import get_db
from backend.models.user import User
from backend.schemas.chat import ChatMessageCreate, ChatMessageResponse
from backend.services.chat_service import ChatService

router = APIRouter(prefix="/chats", dependencies=[Depends(get_current_user)])


@router.post("", response_model=ChatMessageResponse)
async def add_chat_message(
    payload: ChatMessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ChatService(db)
    message = service.add_message(
        student_id=payload.student_id,
        sender=payload.sender,
        message=payload.message,
        user_id=current_user.id,
    )
    return message


@router.get("/{student_id}", response_model=list[ChatMessageResponse])
async def get_chat_history(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ChatService(db)
    service.student_service.ensure_student_profile(student_id, current_user.id)
    return service.get_history(student_id)
