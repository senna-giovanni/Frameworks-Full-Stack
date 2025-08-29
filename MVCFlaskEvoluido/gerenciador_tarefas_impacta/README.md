# Gerenciador de Tarefas (ToDo) - IMPACTA
Projeto entregue para a atividade: Gerenciador de Tarefas com Flask, MVC e SQLite.

## O que tem aqui
- Estrutura MVC com `models/`, `controllers/` e `views/` (templates).
- Banco SQLite: `users.db` (se já existir com usuários, o app reutiliza; caso contrário, um exemplo será criado).
- Modelo `Task` em `models/task.py` com relacionamento Many-to-One com `User`.
- Controller `controllers/task_controller.py` com métodos pedidos: list, create (GET/POST), update status, delete.
- Rotas adicionadas em `app.py` conforme enunciado.
- Templates: `templates/tasks.html` e `templates/create_task.html`.

## Como rodar (passo a passo)
1. Crie e ative um venv (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # linux / mac
   venv\Scripts\activate    # windows
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Se você já tiver um `users.db` (fornecido pelo enunciado), coloque-o na mesma pasta do `app.py` (raiz do projeto).
   Caso NÃO tenha um `users.db`, rode o app e ele criará um exemplo com 3 usuários automaticamente.
4. Executar a aplicação:
   ```bash
   flask run
   ```
   ou
   ```bash
   python app.py
   ```
5. Acesse no navegador: http://127.0.0.1:5000/tasks

## Testes rápidos
- Listar tarefas: GET /tasks
- Criar tarefa: navegue em "Nova Tarefa" ou POST form para /tasks/new
- Concluir tarefa: botão "Concluir" envia POST para /tasks/update/<task_id>
- Excluir tarefa: botão "Excluir" envia POST para /tasks/delete/<task_id>

## Observações sobre entrega
- Entregue por link do repositório no GitHub (coloque esse projeto lá, commit e publique).
- Se quiser, eu já te mostro os comandos git para você subir ao repo.
