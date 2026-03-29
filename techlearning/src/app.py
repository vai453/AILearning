from flask import Flask
from features.user.users import user_bp
from features.student.controller.student_controller import student_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprint
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(student_bp, url_prefix="/api")  # Register student blueprint

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
