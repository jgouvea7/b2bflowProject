from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_contact():
    new_contact = {
        "name": "jonnathas",
        "phone": "5511999999999"
    }

    response = client.post("/v1/contacts", json=new_contact)
    assert response.status_code == 201


def test_delete_all_contacts():
    response = client.delete("/v1/contacts")
    assert response.status_code == 200