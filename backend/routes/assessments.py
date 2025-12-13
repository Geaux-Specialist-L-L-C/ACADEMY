"""Assessment-related endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.jwt_handler import get_current_user
from backend.database import get_db
from backend.models.user import User
from backend.schemas.assessment import AssessmentCreate, AssessmentResponse
from backend.services.assessment_service import AssessmentService

router = APIRouter(prefix="/assessments", dependencies=[Depends(get_current_user)])


@router.post("", response_model=AssessmentResponse)
async def create_assessment(
    payload: AssessmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = AssessmentService(db)
    assessment = service.create_assessment(
        student_id=payload.student_id,
        subject=payload.subject,
        score=payload.score,
        details=payload.details,
        user_id=current_user.id,
    )
    return assessment


@router.get("/{student_id}", response_model=list[AssessmentResponse])
async def list_assessments(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = AssessmentService(db)
    service.student_service.ensure_student_profile(student_id, current_user.id)
    return service.list_assessments(student_id)
