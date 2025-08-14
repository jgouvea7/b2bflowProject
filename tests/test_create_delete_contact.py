import json
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
    body = response.json()
    assert body["message"] == "Contact created successfully"


def test_delete_contact():
    phone_contact = {"phone": "5511999999999"}
    response = client.request(
        method="DELETE",
        url="/v1/contacts/delete-by-phone",
        data=json.dumps(phone_contact),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Contact 'jonnathas' with number 5511999999999 was successfully deleted"


def test_delete_all_logs():
    response = client.delete("/v1/logs")
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Logs were successfully deleted"