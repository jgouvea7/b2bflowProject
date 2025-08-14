from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_contact():
    new_contact = {
        "name": "jonnathas",
        "phone": "5511999999999"
    }

    new_contact2 = {
        "name": "roberto",
        "phone": "5511999999998"
    }

    response = client.post("/v1/contacts", json=new_contact)
    assert response.status_code == 201

    response2 = client.post("/v1/contacts", json=new_contact2)
    assert response2.status_code == 201


def test_send_message():
    response = client.post("/v1/contacts/send-message-all")
    assert response.status_code == 200


def test_delete_all_contacts():
    response = client.delete("/v1/contacts")
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Contacts were successfully deleted"



def test_delete_all_logs():
    response = client.delete("/v1/logs")
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Logs were successfully deleted"