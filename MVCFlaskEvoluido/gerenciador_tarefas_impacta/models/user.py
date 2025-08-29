from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)

    tasks = db.relationship('Task', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.id} {self.name}>'
