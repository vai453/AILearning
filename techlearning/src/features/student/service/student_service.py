from features.student.repository.studentrepository import StudentRepository
from dbconfig.session import get_session


class StudentService:
    def get_student_info(self):
        with get_session() as session:
            repo = StudentRepository(db_session=session)
            return repo.get_all_students()

    def get_student_by_id(self, student_id):
        with get_session() as session:
            repo = StudentRepository(db_session=session)
            return repo.get_student_by_id(student_id)

    def create_student(self, student):
        with get_session() as session:
            repo = StudentRepository(db_session=session)
            return repo.create_student(student)

    def update_student(self, student):
        with get_session() as session:
            repo = StudentRepository(db_session=session)
            return repo.update_student(student)

    def delete_student(self, student_id):
        with get_session() as session:
            repo = StudentRepository(db_session=session)
            return repo.delete_student(student_id)