"""Schemas for assessment endpoints."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class AssessmentCreate(BaseModel):
    student_id: int = Field(..., alias="studentId")
    subject: str
    score: Optional[int] = None
    details: dict[str, Any] = Field(default_factory=dict)

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class AssessmentResponse(BaseModel):
    id: int
    studentId: int = Field(..., alias="student_id")
    subject: str
    status: str
    score: Optional[int] = None
    details: dict[str, Any] = Field(default_factory=dict)
    createdAt: datetime = Field(..., alias="created_at")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        populate_by_name = True
