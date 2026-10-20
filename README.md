# Tasks API (FastAPI + PostgreSQL)

API simples de tarefas

## Configuração

Única variável de ambiente:

```
DATABASE_URL=postgresql+psycopg2://USUARIO:SENHA@HOST:5432/BANCO
```

(Se não definida, usa `postgresql+psycopg2://app:app@localhost:5432/appdb`.)

As tabelas são criadas automaticamente na inicialização. Se o banco
estiver inacessível, a aplicação falha ao subir.

## Rodar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Docs interativas em `/docs`.

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/health` | Liveness (não toca no banco) |
| GET | `/ready` | Readiness (faz `SELECT 1` no banco) |
| POST | `/tasks` | Cria tarefa |
| GET | `/tasks` | Lista (`skip`, `limit`) |
| GET | `/tasks/{id}` | Busca |
| PATCH | `/tasks/{id}` | Atualiza |
| DELETE | `/tasks/{id}` | Remove |

## Testes (usam SQLite)

```bash
pip install pytest httpx
pytest
```
