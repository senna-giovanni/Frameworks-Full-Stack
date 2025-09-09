from flask import Flask, request, jsonify, make_response
from flasgger import Swagger

app = Flask(__name__)

# Configuração segura do Swagger sem sobrepor a rota "/"
#swagger = Swagger(app, config={
#    "headers": [],
#    "specs": [
#        {
#            "endpoint": 'apispec',
#            "route": '/apispec.json',
#            "rule_filter": lambda rule: True,
#            "model_filter": lambda tag: True,
#        }
#    ],
#    "swagger_ui": True,
#    "specs_route": "/apidocs/"
#})

# -------------------------------
# Dados em memória
# -------------------------------
users = []
current_id = 1

def _next_id():
    global current_id
    _id = current_id
    current_id += 1
    return _id

def _find_user_by_id(user_id):
    return next((u for u in users if u["id"] == user_id), None)

# -------------------------------
# Funções de resposta JSON
# -------------------------------
def json_created(payload):
    return make_response(jsonify(payload), 201)

def json_ok(payload):
    return make_response(jsonify(payload), 200)

def json_error(message, status_code=400):
    return make_response(jsonify({"error": message}), status_code)

# -------------------------------
# Rotas
# -------------------------------
@app.route("/", methods=["GET"])
def home():
    """
    Página inicial da API
    ---
    responses:
      200:
        description: Mensagem de boas-vindas
    """
    return jsonify({"message": "Bem-vindo à API! Acesse /apidocs para a documentação."})

@app.post("/users")
def create_user():
    """
    Cria um novo usuário
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
              email:
                type: string
            required:
              - nome
              - email
    responses:
      201:
        description: Usuário criado
      400:
        description: Requisição inválida
    """
    data = request.get_json()
    if not data or "nome" not in data or "email" not in data:
        return json_error("Campos 'nome' e 'email' são obrigatórios.", 400)
    user = {"id": _next_id(), "nome": data["nome"].strip(), "email": data["email"].strip()}
    users.append(user)
    return json_created(user)

@app.get("/users")
def list_users():
    """
    Lista todos os usuários
    ---
    responses:
      200:
        description: Lista de usuários
    """
    return json_ok(users)

@app.get("/users/<int:user_id>")
def get_user(user_id):
    """
    Busca usuário por ID
    ---
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Usuário encontrado
      404:
        description: Usuário não encontrado
    """
    user = _find_user_by_id(user_id)
    if not user:
        return json_error("Usuário não encontrado.", 404)
    return json_ok(user)

@app.put("/users/<int:user_id>")
def update_user(user_id):
    """
    Atualiza usuário existente
    ---
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
              email:
                type: string
    responses:
      200:
        description: Usuário atualizado
      404:
        description: Usuário não encontrado
    """
    user = _find_user_by_id(user_id)
    if not user:
        return json_error("Usuário não encontrado.", 404)
    data = request.get_json()
    if "nome" in data:
        user["nome"] = data["nome"].strip()
    if "email" in data:
        user["email"] = data["email"].strip()
    return json_ok(user)

@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    """
    Exclui usuário existente
    ---
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Usuário excluído
      404:
        description: Usuário não encontrado
    """
    user = _find_user_by_id(user_id)
    if not user:
        return json_error("Usuário não encontrado.", 404)
    users.remove(user)
    return json_ok({"message": "Usuário excluído com sucesso"})

# -------------------------------
# Rodar app
# -------------------------------


  @app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Rota não encontrada"}), 404

if __name__ == "__main__":
    print("Rotas registradas:", app.url_map)
    app.run(host="0.0.0.0", port=5000, debug=True)
