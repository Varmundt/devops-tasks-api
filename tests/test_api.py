import os

# Usa SQLite nos testes: rápidos e sem depender de um Postgres rodando.
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app.database import Base, engine  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture()
def client():
    Base.metadata.drop_all(bind=engine)
    with TestClient(app) as c:
        yield c


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_ready(client):
    assert client.get("/ready").status_code == 200


def test_task_crud(client):
    created = client.post("/tasks", json={"title": "Estudar Docker"})
    assert created.status_code == 201
    task_id = created.json()["id"]

    assert client.get(f"/tasks/{task_id}").json()["title"] == "Estudar Docker"
    assert len(client.get("/tasks").json()) == 1

    updated = client.patch(f"/tasks/{task_id}", json={"done": True})
    assert updated.json()["done"] is True

    assert client.delete(f"/tasks/{task_id}").status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404


def test_validation(client):
    assert client.post("/tasks", json={"title": ""}).status_code == 422
