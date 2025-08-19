# API Simples de Usuários - Flask

## Descrição
Esta é uma API RESTful desenvolvida em Flask para gerenciar usuários.  
Permite criar, listar, atualizar e deletar usuários em memória, sem a necessidade de banco de dados.

---

## Como executar

1. Abra a pasta do projeto no VS Code ou outro editor de sua preferência.  
2. Instale as dependências (garantindo que tenha Python 3 instalado):
```bash
pip install -r requirements.txt
```
3. Execute a API:
```bash
python app.py
```
4. A aplicação ficará disponível em `http://localhost:5000`.

---

## Endpoints

### Criar usuário
```http
POST /users
```
**Body JSON:**
```json
{
  "nome": "GIovanni Senna",
  "email": "Giovanni@exemplo.com"
}
```

### Listar usuários
```http
GET /users
```

### Buscar usuário por ID
```http
GET /users/<id>
```

### Atualizar usuário
```http
PUT /users/<id>
```
**Body JSON (parcial ou completo):**
```json
{
  "nome": "Novo Nome",
  "email": "novoemail@exemplo.com"
}
```

### Excluir usuário
```http
DELETE /users/<id>
```

---

## Exemplo de resposta
```json
{
  "id": 1,
  "nome": "Giovanni Senna",
  "email": "Giovanni@exemplo.com"
}
```

---

## Grupo 07
Entrega da atividade **Construção de API Simples com Flask**  
Grupo 07 - Giovanni Senna Ferreira SI 4A
          Enzo Scartezini Gropo SI 4A
          Yuri Souza Tito ADS 4B
