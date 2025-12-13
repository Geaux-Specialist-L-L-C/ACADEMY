"""SQLAlchemy model for student profiles used in dashboards and assessments."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.models.user import Base


class StudentProfile(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    parent_id = Column(Integer, nullable=True)
    name = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    learning_style = Column(String, nullable=True)
    has_taken_assessment = Column(Boolean, default=False, nullable=False)
    assessment_status = Column(String, default="pending", nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    learning_plans = relationship("LearningPlan", back_populates="student")
    assessments = relationship("Assessment", back_populates="student")
    chat_messages = relationship("ChatMessage", back_populates="student")
