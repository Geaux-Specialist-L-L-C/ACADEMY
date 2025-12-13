"""Service to manage assessments and track completion."""

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from backend.models.assessment import Assessment
from backend.services.student_service import StudentService


class AssessmentService:
    def __init__(self, db: Session):
        self.db = db
        self.student_service = StudentService(db)

    def create_assessment(
        self,
        student_id: int,
        subject: str,
        user_id: int,
        score: Optional[int] = None,
        details: Optional[dict] = None,
    ) -> Assessment:
        student = self.student_service.ensure_student_profile(student_id, user_id)
        assessment = Assessment(
            student_id=student.id,
            subject=subject,
            status="completed" if score is not None else "in_progress",
            score=score,
            details=details or {},
            created_at=datetime.utcnow(),
        )
        student.has_taken_assessment = True
        student.assessment_status = assessment.status
        self.db.add(assessment)
        self.db.commit()
        self.db.refresh(assessment)
        return assessment

    def list_assessments(self, student_id: int) -> list[Assessment]:
        return (
            self.db.query(Assessment)
            .filter(Assessment.student_id == student_id)
            .order_by(Assessment.created_at.desc())
            .all()
        )
