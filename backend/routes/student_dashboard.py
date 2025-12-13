"""Routes serving student dashboard data."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.auth.jwt_handler import get_current_user
from backend.database import get_db
from backend.models.user import User
from backend.schemas.student_dashboard import (
    LearningStyleUpdate,
    StudentDashboardResponse,
)
from backend.services.student_service import StudentService

router = APIRouter(prefix="/students", dependencies=[Depends(get_current_user)])


@router.get("/{student_id}/dashboard", response_model=StudentDashboardResponse)
async def get_student_dashboard(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = StudentService(db)
    student = service.ensure_student_profile(student_id, current_user.id)
    payload = service.build_dashboard_payload(student)
    return payload


@router.post("/{student_id}/learning-style", response_model=StudentDashboardResponse)
async def update_learning_style(
    student_id: int,
    learning_style: LearningStyleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = StudentService(db)
    try:
        service.record_learning_style(student_id, learning_style.learningStyle)
    except ValueError:
        raise HTTPException(status_code=404, detail="Student not found")
    student = service.ensure_student_profile(student_id, current_user.id)
    return service.build_dashboard_payload(student)
