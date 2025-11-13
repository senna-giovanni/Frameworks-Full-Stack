from extensions import db

class Food(db.Model):
    __tablename__ = "foods"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    calorias = db.Column(db.Float, nullable=False)
    proteinas = db.Column(db.Float, nullable=False)
    carboidratos = db.Column(db.Float, nullable=False)
    gorduras = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "calorias": self.calorias,
            "proteinas": self.proteinas,
            "carboidratos": self.carboidratos,
            "gorduras": self.gorduras
        }
