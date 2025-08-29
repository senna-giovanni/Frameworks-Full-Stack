from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-me'
db_path = os.path.join(os.path.dirname(__file__), 'users.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from models.user import User
from models.task import Task


with app.app_context():
    db.create_all()
    
    if User.query.count() == 0:
        u1 = User(name='Alice Silva', email='alice@example.com')
        u2 = User(name='Bruno Costa', email='bruno@example.com')
        u3 = User(name='Carla Souza', email='carla@example.com')
        db.session.add_all([u1,u2,u3])
        db.session.commit()


from controllers.task_controller import TaskController


app.add_url_rule('/tasks', view_func=TaskController.list_tasks, methods=['GET'])
app.add_url_rule('/tasks/new', view_func=TaskController.create_task, methods=['GET','POST'])
app.add_url_rule('/tasks/update/<int:task_id>', view_func=TaskController.update_task_status, methods=['POST'])
app.add_url_rule('/tasks/delete/<int:task_id>', view_func=TaskController.delete_task, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
