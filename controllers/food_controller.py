from extensions import db
from models.food import Food
from flask import jsonify, request

def create_food(data):
    if not data or not all(key in data for key in ("nome", "calorias", "proteinas", "carboidratos", "gorduras")):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400
    food = Food(
        nome=data["nome"].strip(),
        calorias=data["calorias"],
        proteinas=data["proteinas"],
        carboidratos=data["carboidratos"],
        gorduras=data["gorduras"]
    )
    db.session.add(food)
    db.session.commit()
    return jsonify(food.to_dict()), 201

def list_foods():
    foods = Food.query.all()
    return jsonify([f.to_dict() for f in foods]), 200

def get_food(food_id):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({"error": "Alimento não encontrado."}), 404
    return jsonify(food.to_dict()), 200

def update_food(food_id, data):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({"error": "Alimento não encontrado."}), 404
    for field in ("nome", "calorias", "proteinas", "carboidratos", "gorduras"):
        if field in data:
            setattr(food, field, data[field])
    db.session.commit()
    return jsonify(food.to_dict()), 200

def delete_food(food_id):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({"error": "Alimento não encontrado."}), 404
    db.session.delete(food)
    db.session.commit()
    return jsonify({"message": "Alimento excluído com sucesso."}), 200
