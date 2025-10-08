from app import db
from models.task import Task
from models.user import User
from flask import jsonify

def create_task(data):
    if not data or "titulo" not in data or "user_id" not in data:
        return jsonify({"error":"Campos 'titulo' e 'user_id' são obrigatórios."}), 400
    user = User.query.get(data["user_id"])
    if not user:
        return jsonify({"error":"Usuário não encontrado para 'user_id' fornecido."}), 404
    task = Task(titulo=data["titulo"].strip(), descricao=data.get("descricao"), concluida=bool(data.get("concluida", False)), user_id=user.id)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

def list_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200

def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error":"Tarefa não encontrada."}), 404
    return jsonify(task.to_dict()), 200

def update_task(task_id, data):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error":"Tarefa não encontrada."}), 404
    if "titulo" in data:
        task.titulo = data["titulo"].strip()
    if "descricao" in data:
        task.descricao = data["descricao"]
    if "concluida" in data:
        task.concluida = bool(data["concluida"])
    db.session.commit()
    return jsonify(task.to_dict()), 200

def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error":"Tarefa não encontrada."}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message":"Tarefa excluída com sucesso."}), 200
