from flask import Blueprint, jsonify, request
from features.student.service.student_service import StudentService
from features.student.model.student import Student
from features.student.schemas.student_schema import StudentSchema
from pydantic import ValidationError

student_bp = Blueprint("student_bp", __name__)
student_service = StudentService()


class StudentController:
    @student_bp.route("/createstudents", methods=["POST"])
    def create_student():
        try:
            data = request.get_json()
            schema = StudentSchema(**data)
            student = Student(schema)
            
            result = student_service.create_student(student)
            response = StudentSchema.from_orm(result)
            return jsonify(response.model_dump(mode='json')), 201
        except ValidationError as e:
            return jsonify({"error": "Invalid request data", "details": e.errors()}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @student_bp.route("/getstudents", methods=["GET"])
    def get_student_info():
        try:
            result = student_service.get_student_info()
            response_data = [StudentSchema.from_orm(student).model_dump(mode='json') for student in result]
            return jsonify(response_data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @student_bp.route("/students/<int:student_id>", methods=["GET"])
    def get_student_by_id(student_id):
        try:
            result = student_service.get_student_by_id(student_id)
            if not result:
                return jsonify({"error": "Student not found"}), 404
            
            response = StudentSchema.from_orm(result)
            return jsonify(response.model_dump(mode='json')), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @student_bp.route("/students/<int:student_id>", methods=["PUT"])
    def update_student(student_id):
        try:
            data = request.get_json()
            schema = StudentSchema(**data)
            
            result = student_service.get_student_by_id(student_id)
            if not result:
                return jsonify({"error": "Student not found"}), 404
            
            # Update fields from schema if they have values
            for field in ['name', 'dob', 'address', 'course', 'batch']:
                val = getattr(schema, field)
                if val is not None:
                    setattr(result, field, val)
            
            updated = student_service.update_student(result)
            response = StudentSchema.from_orm(updated)
            return jsonify(response.model_dump(mode='json')), 200
        except ValidationError as e:
            return jsonify({"error": "Invalid request data", "details": e.errors()}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @student_bp.route("/students/<int:student_id>", methods=["DELETE"])
    def delete_student(student_id):
        try:
            result = student_service.delete_student(student_id)
            if not result:
                return jsonify({"error": "Student not found"}), 404
            
            return jsonify({"message": "Student deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500