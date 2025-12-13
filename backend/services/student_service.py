"""Service layer for student dashboard data."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy.orm import Session

from backend.models.assessment import Assessment
from backend.models.learning_plan import LearningPlan
from backend.models.student_profile import StudentProfile


class StudentService:
    """Encapsulates student-related business logic for dashboards."""

    def __init__(self, db: Session):
        self.db = db

    def get_student(self, student_id: int) -> StudentProfile | None:
        return (
            self.db.query(StudentProfile)
            .filter(StudentProfile.id == student_id)
            .first()
        )

    def ensure_student_profile(self, student_id: int, user_id: int) -> StudentProfile:
        """Return a student profile or create a placeholder one tied to the user."""

        student = self.get_student(student_id)
        if student:
            return student

        student = StudentProfile(
            id=student_id,
            user_id=user_id,
            name=f"Student {student_id}",
            grade="N/A",
            has_taken_assessment=False,
            assessment_status="pending",
        )
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def record_learning_style(self, student_id: int, learning_style: str) -> StudentProfile:
        student = self.get_student(student_id)
        if not student:
            raise ValueError("Student not found")

        student.learning_style = learning_style
        student.has_taken_assessment = True
        student.assessment_status = "completed"
        student.updated_at = datetime.utcnow()
        self.db.commit()
        self.db.refresh(student)
        return student

    def build_dashboard_payload(self, student: StudentProfile) -> dict:
        """Aggregate dashboard data expected by the frontend."""

        assessments = (
            self.db.query(Assessment)
            .filter(Assessment.student_id == student.id)
            .order_by(Assessment.created_at.desc())
            .all()
        )
        learning_plans = (
            self.db.query(LearningPlan)
            .filter(LearningPlan.student_id == student.id)
            .order_by(LearningPlan.created_at.desc())
            .all()
        )

        recent_activities = [
            {
                "id": assessment.id,
                "type": "assessment",
                "name": assessment.subject,
                "date": assessment.created_at,
            }
            for assessment in assessments[:5]
        ] + [
            {
                "id": plan.id,
                "type": "learning_plan",
                "name": "Learning Plan",
                "date": plan.created_at,
            }
            for plan in learning_plans[:5]
        ]

        completed_scores = [a.score for a in assessments if a.score is not None]
        average_score = (
            sum(completed_scores) / len(completed_scores) if completed_scores else 0
        )
        progress = [
            {"type": "Assessments Completed", "value": len(assessments)},
            {"type": "Average Score", "value": round(average_score, 2)},
        ]

        learning_style = None
        if student.learning_style:
            learning_style = {
                "type": student.learning_style,
                "strengths": [],
                "recommendations": [],
            }

        return {
            "id": student.id,
            "parent_id": student.parent_id,
            "name": student.name,
            "grade": student.grade,
            "learning_style": learning_style,
            "has_taken_assessment": student.has_taken_assessment,
            "assessment_status": student.assessment_status,
            "recentActivities": recent_activities,
            "progress": progress,
        }
