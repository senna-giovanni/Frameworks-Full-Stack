from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

users = []
current_id = 1

def _next_id():
    global current_id
    _id = current_id
    current_id += 1
    return _id

def _find_user_by_id(user_id):
    return next((u for u in users if u["id"] == user_id), None)

def json_created(payload):
    return make_response(jsonify(payload), 201)

def json_ok(payload):
    return make_response(jsonify(payload), 200)

def json_error(message, status_code=400):
    return make_response(jsonify({"error": message}), status_code)

@app.post('/users')
def create_user():
    data = request.get_json(silent=True)
    if not data:
        return json_error("Corpo da requisição deve ser JSON.", 400)
    nome = data.get("nome")
    email = data.get("email")
    if not isinstance(nome, str) or not nome.strip():
        return json_error("Campo 'nome' é obrigatório.", 400)
    if not isinstance(email, str) or not email.strip():
        return json_error("Campo 'email' é obrigatório.", 400)
    user = {"id": _next_id(), "nome": nome.strip(), "email": email.strip()}
    users.append(user)
    return json_created(user)

@app.get('/users')
def list_users():
    return json_ok(users)

@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = _find_user_by_id(user_id)
    if not user:
        return json_error("Usuário não encontrado.", 404)
    return json_ok(user)

@app.put('/users/<int:user_id>')
def update_user(user_id):
    user = _find_user_by_id(user_id)
    if not user:
        return json_error("Usuário não encontrado.", 404)
    data = request.get_json(silent=True)
    if data is None:
        return json_error("Corpo da requisição deve ser JSON.", 400)
    if "nome" in data:
        if not isinstance(data["nome"], str) or not data["nome"].strip():
            return json_error("Campo 'nome' inválido.", 400)
        user["nome"] = data["nome"].strip()
    if "email" in data:
        if not isinstance(data["email"], str) or not data["email"].strip():
            return json_error("Campo 'email' inválido.", 400)
        user["email"] = data["email"].strip()
    return json_ok(user)

@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user = _find_user_by_id(user_id)
    if not user:
        return json_error("Usuário não encontrado.", 404)
    users.remove(user)
    return json_ok({"message": "Usuário excluído com sucesso"})

@app.errorhandler(404)
def handle_404(e):
    return json_error("Recurso não encontrado.", 404)

@app.errorhandler(405)
def handle_405(e):
    return json_error("Método não permitido.", 405)

@app.errorhandler(400)
def handle_400(e):
    return json_error("Requisição inválida.", 400)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
