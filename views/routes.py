from flask import Blueprint, request
from controllers.user_controller import create_user, list_users, get_user, update_user, delete_user
from controllers.food_controller import create_food, list_foods, get_food, update_food, delete_food

main_bp = Blueprint("main", __name__)

# Usuários
main_bp.route("/users", methods=["POST"])(lambda: create_user(request.get_json()))
main_bp.route("/users", methods=["GET"])(lambda: list_users())
main_bp.route("/users/<int:user_id>", methods=["GET"])(lambda user_id: get_user(user_id))
main_bp.route("/users/<int:user_id>", methods=["PUT"])(lambda user_id: update_user(user_id, request.get_json()))
main_bp.route("/users/<int:user_id>", methods=["DELETE"])(lambda user_id: delete_user(user_id))

# Alimentos
main_bp.route("/alimentos", methods=["POST"])(lambda: create_food(request.get_json()))
main_bp.route("/alimentos", methods=["GET"])(lambda: list_foods())
main_bp.route("/alimentos/<int:food_id>", methods=["GET"])(lambda food_id: get_food(food_id))
main_bp.route("/alimentos/<int:food_id>", methods=["PUT"])(lambda food_id: update_food(food_id, request.get_json()))
main_bp.route("/alimentos/<int:food_id>", methods=["DELETE"])(lambda food_id: delete_food(food_id))
