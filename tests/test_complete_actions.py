from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_contact():
    new_contact = {
        "name": "jonnathas",
        "phone": "5511952937705"
    }

    response = client.post("/v1/contacts", json=new_contact)
    assert response.status_code == 201


def test_send_message():
    contact = {
        "phone": "5511952937705"
    }

    response = client.post("/v1/contacts/send-message", json=contact)
    assert response.status_code == 200


def test_delete_all_contacts():
    response = client.delete("/v1/contacts")
    assert response.status_code == 200