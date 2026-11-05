# Tasks API (FastAPI + PostgreSQL)

API CRUD básica para anotação de tarefas, utilizada como base para estudos de DevOps com Docker, Docker Compose e PostgreSQL.

## Stack

- Python 3.12 + FastAPI
- SQLAlchemy 2 + psycopg2
- PostgreSQL 16
- Docker e Docker Compose

## Configuração

Copie o arquivo de exemplo e ajuste os valores (principalmente a senha):

```bash
cp .env.example .env          # Linux/macOS
copy .env.example .env        # Windows (cmd/PowerShell)
```

Variáveis utilizadas:

| Variável | Descrição |
|---|---|
| `POSTGRES_USER` | Usuário criado no Postgres |
| `POSTGRES_PASSWORD` | Senha do usuário |
| `POSTGRES_DB` | Nome do banco criado |
| `DATABASE_URL` | String de conexão usada pela API |

Formato da `DATABASE_URL`:

```
postgresql+psycopg2://USUARIO:SENHA@HOST:5432/BANCO
```

A `DATABASE_URL` é **obrigatória**: sem ela, a aplicação não sobe. Com o Docker Compose, o `HOST` é o nome do serviço do banco (`db`).

As tabelas são criadas automaticamente na inicialização. Se o banco estiver inacessível, a aplicação falha ao subir.

## Rodar com Docker Compose

```bash
docker compose up -d --build
```

- API: http://localhost:8000
- Documentação interativa: http://localhost:8000/docs

O serviço `db` possui healthcheck, e a API só inicia depois que o banco estiver saudável. Os dados ficam no volume `pgdata` e persistem entre reinicializações.

## Rodar localmente (sem Docker para a API)

Requer um PostgreSQL acessível e a `DATABASE_URL` apontando para ele (o host deve ser `localhost` ou o endereço do banco, e não `db`).

```bash
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

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

Exemplo:

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar Docker"}'
```