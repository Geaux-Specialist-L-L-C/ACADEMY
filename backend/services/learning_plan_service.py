"""Service for managing learning plans."""

from datetime import datetime

from sqlalchemy.orm import Session

from backend.models.learning_plan import LearningPlan
from backend.services.student_service import StudentService


class LearningPlanService:
    def __init__(self, db: Session):
        self.db = db
        self.student_service = StudentService(db)

    def create_plan(self, student_id: int, prompt: str, user_id: int) -> LearningPlan:
        student = self.student_service.ensure_student_profile(student_id, user_id)
        generated_plan = self._build_plan_from_prompt(prompt)
        plan = LearningPlan(
            student_id=student.id,
            prompt=prompt,
            plan=generated_plan,
            created_at=datetime.utcnow(),
        )
        self.db.add(plan)
        self.db.commit()
        self.db.refresh(plan)
        return plan

    def list_plans(self, student_id: int) -> list[LearningPlan]:
        return (
            self.db.query(LearningPlan)
            .filter(LearningPlan.student_id == student_id)
            .order_by(LearningPlan.created_at.desc())
            .all()
        )

    def _build_plan_from_prompt(self, prompt: str) -> str:
        bullet_points = [
            "Review core concepts with curated reading assignments.",
            "Practice with interactive exercises three times a week.",
            "Schedule weekly reflections to track understanding.",
        ]
        formatted_points = "\n".join(f"- {point}" for point in bullet_points)
        return f"Custom plan based on: {prompt}\n{formatted_points}"
