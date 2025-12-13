"""Service layer for storing and retrieving chat history."""

from datetime import datetime

from sqlalchemy.orm import Session

from backend.models.chat_message import ChatMessage
from backend.services.student_service import StudentService


class ChatService:
    def __init__(self, db: Session):
        self.db = db
        self.student_service = StudentService(db)

    def add_message(self, student_id: int, sender: str, message: str, user_id: int) -> ChatMessage:
        student = self.student_service.ensure_student_profile(student_id, user_id)
        chat_message = ChatMessage(
            student_id=student.id,
            sender=sender,
            message=message,
            created_at=datetime.utcnow(),
        )
        self.db.add(chat_message)
        self.db.commit()
        self.db.refresh(chat_message)
        return chat_message

    def get_history(self, student_id: int, limit: int = 50) -> list[ChatMessage]:
        return (
            self.db.query(ChatMessage)
            .filter(ChatMessage.student_id == student_id)
            .order_by(ChatMessage.created_at.asc())
            .limit(limit)
            .all()
        )
