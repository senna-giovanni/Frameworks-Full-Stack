from flask import Blueprint, request
from flasgger import swag_from
from controllers.user_controller import create_user, list_users, get_user, update_user, delete_user
from controllers.task_controller import create_task, list_tasks, get_task, update_task, delete_task

main_bp = Blueprint("main", __name__)

@main_bp.route("/users", methods=["POST"])
@swag_from({
    'responses': {201: {'description': 'Usuário criado'}, 400: {'description': 'Dados inválidos'}}
})
def route_create_user():
    return create_user(request.get_json())

@main_bp.route("/users", methods=["GET"])
def route_list_users():
    return list_users()

@main_bp.route("/users/<int:user_id>", methods=["GET"])
def route_get_user(user_id):
    return get_user(user_id)

@main_bp.route("/users/<int:user_id>", methods=["PUT"])
def route_update_user(user_id):
    return update_user(user_id, request.get_json())

@main_bp.route("/users/<int:user_id>", methods=["DELETE"])
def route_delete_user(user_id):
    return delete_user(user_id)

@main_bp.route("/tasks", methods=["POST"])
def route_create_task():
    return create_task(request.get_json())

@main_bp.route("/tasks", methods=["GET"])
def route_list_tasks():
    return list_tasks()

@main_bp.route("/tasks/<int:task_id>", methods=["GET"])
def route_get_task(task_id):
    return get_task(task_id)

@main_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def route_update_task(task_id):
    return update_task(task_id, request.get_json())

@main_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def route_delete_task(task_id):
    return delete_task(task_id)
