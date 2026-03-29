
from unittest import result
from features.student.model.student import Student


class StudentRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_students(self):
        result= self.db_session.query(Student).all()
        return result

    def get_student_by_id(self, student_id):
        return (
            self.db_session.query(Student)
            .filter(Student.id == student_id)
            .first()
        )

    def create_student(self, student):
        # Ensure DB-generated values (PK, server defaults) are populated
        self.db_session.add(student)
        try:
            self.db_session.flush()
            self.db_session.refresh(student)
        except Exception:
            # let context manager rollback and propagate
            raise
        return student

    def update_student(self, student):
        existing = self.get_student_by_id(student.id)
        if not existing:
            return None
        # copy allowed fields from incoming `student` to the existing instance
        for attr in ("name", "dob", "address", "course", "batch"):
            if hasattr(student, attr):
                setattr(existing, attr, getattr(student, attr))
        try:
            self.db_session.flush()
            self.db_session.refresh(existing)
        except Exception:
            raise
        return existing

    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if not student:
            return False
        self.db_session.delete(student)
        try:
            self.db_session.flush()
        except Exception:
            raise
        return True