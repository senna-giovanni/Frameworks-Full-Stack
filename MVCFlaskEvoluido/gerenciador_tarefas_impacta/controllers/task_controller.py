from flask import request, jsonify
from models.task import Task
from models.user import User
from app import db

class TaskController:

    @staticmethod
    def list_tasks():
        """
        Listar todas as tarefas
        ---
        tags:
          - Tasks
        responses:
          200:
            description: Lista de tarefas
            schema:
              type: array
              items:
                properties:
                  id:
                    type: integer
                  title:
                    type: string
                  done:
                    type: boolean
                  user_id:
                    type: integer
        """
        tasks = Task.query.all()
        result = [
            {"id": t.id, "title": t.title, "done": t.done, "user_id": t.user_id}
            for t in tasks
        ]
        return jsonify(result), 200

    @staticmethod
    def create_task():
        """
        Criar uma nova tarefa
        ---
        tags:
          - Tasks
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - title
                - user_id
              properties:
                title:
                  type: string
                user_id:
                  type: integer
        responses:
          201:
            description: Tarefa criada com sucesso
        """
        data = request.get_json()
        title = data.get("title")
        user_id = data.get("user_id")

        if not title or not user_id:
            return jsonify({"error": "Campos title e user_id são obrigatórios"}), 400

        task = Task(title=title, user_id=user_id, done=False)
        db.session.add(task)
        db.session.commit()

        return jsonify({"message": "Tarefa criada", "id": task.id}), 201

    @staticmethod
    def update_task(task_id):
        """
        Atualizar uma tarefa existente
        ---
        tags:
          - Tasks
        parameters:
          - name: task_id
            in: path
            type: integer
            required: true
          - in: body
            name: body
            required: true
            schema:
              type: object
              properties:
                title:
                  type: string
                done:
                  type: boolean
        responses:
          200:
            description: Tarefa atualizada
          404:
            description: Tarefa não encontrada
        """
        task = Task.query.get(task_id)
        if not task:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        data = request.get_json()
        task.title = data.get("title", task.title)
        task.done = data.get("done", task.done)

        db.session.commit()
        return jsonify({"message": "Tarefa atualizada"}), 200

    @staticmethod
    def delete_task(task_id):
        """
        Excluir uma tarefa
        ---
        tags:
          - Tasks
        parameters:
          - name: task_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Tarefa excluída com sucesso
          404:
            description: Tarefa não encontrada
        """
        task = Task.query.get(task_id)
        if not task:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Tarefa excluída"}), 200
