"""Pydantic schemas for student dashboard data."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class LearningStyleSchema(BaseModel):
    type: Optional[str] = None
    strengths: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)


class ActivitySchema(BaseModel):
    id: Optional[int] = None
    type: str
    name: str
    date: datetime


class ProgressMetric(BaseModel):
    type: str
    value: float


class LearningStyleUpdate(BaseModel):
    learningStyle: str

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class StudentDashboardResponse(BaseModel):
    id: int
    parentId: Optional[int] = Field(None, alias="parent_id")
    name: str
    grade: str
    learningStyle: Optional[LearningStyleSchema] = Field(None, alias="learning_style")
    hasTakenAssessment: bool = Field(False, alias="has_taken_assessment")
    assessmentStatus: Optional[str] = Field(None, alias="assessment_status")
    recentActivities: list[ActivitySchema] = Field(default_factory=list)
    progress: list[ProgressMetric] = Field(default_factory=list)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        populate_by_name = True
