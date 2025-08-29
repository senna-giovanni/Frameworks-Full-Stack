from flask import render_template, request, redirect, url_for, flash
from app import db
from models.task import Task
from models.user import User

class TaskController:
    @staticmethod
    def list_tasks():
        tasks = Task.query.order_by(Task.id.desc()).all()
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'GET':
            users = User.query.all()
            return render_template('create_task.html', users=users)
      
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        user_id = request.form.get('user_id')
        if not title:
            flash('Título é obrigatório.', 'error')
            users = User.query.all()
            return render_template('create_task.html', users=users)
        try:
            user_id = int(user_id)
        except (TypeError, ValueError):
            flash('Usuário inválido.', 'error')
            users = User.query.all()
            return render_template('create_task.html', users=users)

        user = User.query.get(user_id)
        if not user:
            flash('Usuário não encontrado.', 'error')
            users = User.query.all()
            return render_template('create_task.html', users=users)

        task = Task(title=title, description=description or None, user_id=user.id)
        db.session.add(task)
        db.session.commit()
        flash('Tarefa criada com sucesso.', 'success')
        return redirect(url_for('TaskController_list_tasks'))

    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get(task_id)
        if not task:
            flash('Tarefa não encontrada.', 'error')
            return redirect(url_for('TaskController_list_tasks'))
        # toggle
        task.status = 'Concluído' if task.status == 'Pendente' else 'Pendente'
        db.session.commit()
        flash('Status atualizado.', 'success')
        return redirect(url_for('TaskController_list_tasks'))

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if not task:
            flash('Tarefa não encontrada.', 'error')
            return redirect(url_for('TaskController_list_tasks'))
        db.session.delete(task)
        db.session.commit()
        flash('Tarefa excluída.', 'success')
        return redirect(url_for('TaskController_list_tasks'))


