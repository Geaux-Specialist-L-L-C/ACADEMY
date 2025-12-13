"""Endpoints for creating and retrieving learning plans."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.jwt_handler import get_current_user
from backend.database import get_db
from backend.models.user import User
from backend.schemas.learning_plan import LearningPlanCreate, LearningPlanResponse
from backend.services.learning_plan_service import LearningPlanService

router = APIRouter(prefix="/learning-plans", dependencies=[Depends(get_current_user)])


@router.post("", response_model=LearningPlanResponse)
async def create_learning_plan(
    payload: LearningPlanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = LearningPlanService(db)
    plan = service.create_plan(
        student_id=payload.student_id,
        prompt=payload.prompt,
        user_id=current_user.id,
    )
    return plan


@router.get("/{student_id}", response_model=list[LearningPlanResponse])
async def list_learning_plans(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = LearningPlanService(db)
    # ensure student exists for the requesting user
    service.student_service.ensure_student_profile(student_id, current_user.id)
    return service.list_plans(student_id)
