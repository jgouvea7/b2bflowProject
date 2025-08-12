from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_contacts():
    response = client.get("/v1/contacts")
    assert response.status_code == 200
    assert response.json() == []