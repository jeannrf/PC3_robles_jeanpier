from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_sumar_integracion():
    response = client.get("/sumar", params={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"resultado": 7}


def test_promedio_lista_valida():
    response = client.post("/promedio", json={"valores": [2, 4, 6]})
    assert response.status_code == 200
    assert response.json() == {"promedio": 4}


def test_promedio_lista_vacia():
    response = client.post("/promedio", json={"valores": []})
    assert response.status_code == 400
    assert response.json() == {"detail": "Lista vacia"}


def test_todos_los_endpoints():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/sumar", params={"a": 1, "b": 2}).json() == {"resultado": 3}
    assert client.post("/promedio", json={"valores": [1, 3]}).json() == {"promedio": 2}
