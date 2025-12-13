"""Schemas for chat history endpoints."""

from datetime import datetime

from pydantic import BaseModel, Field


class ChatMessageCreate(BaseModel):
    student_id: int = Field(..., alias="studentId")
    sender: str
    message: str

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class ChatMessageResponse(BaseModel):
    id: int
    studentId: int = Field(..., alias="student_id")
    sender: str
    message: str
    createdAt: datetime = Field(..., alias="created_at")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        populate_by_name = True
