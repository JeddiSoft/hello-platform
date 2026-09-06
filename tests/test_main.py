from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_hello():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "hello-platform"
    assert data["version"] == "1.0.0"
    assert data["message"] == "Hello from GitOps end to end"
    #assert data["message"] == "ESTO_TIENE_QUE_FALLAR"

def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"