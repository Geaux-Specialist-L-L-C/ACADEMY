"""Pydantic schemas for learning plan endpoints."""

from datetime import datetime
from pydantic import BaseModel, Field


class LearningPlanCreate(BaseModel):
    student_id: int = Field(..., alias="studentId")
    prompt: str

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class LearningPlanResponse(BaseModel):
    id: int
    studentId: int = Field(..., alias="student_id")
    prompt: str
    plan: str
    createdAt: datetime = Field(..., alias="created_at")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        populate_by_name = True
