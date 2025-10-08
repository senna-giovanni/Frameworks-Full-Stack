from extensions import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="user", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}
