from flask import Blueprint, jsonify, request

user_bp = Blueprint("user_bp", __name__)

users = [{"id": 1, "name": "Raj"}, {"id": 2, "name": "Amit"}]


@user_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify({"success": True, "data": users}), 200


@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    new_user = {"id": len(users) + 1, "name": data.get("name")}

    users.append(new_user)

    return jsonify({"success": True, "message": "User created", "data": new_user}), 201


@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200


@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]

    return jsonify({"message": "User deleted successfully"}), 200
