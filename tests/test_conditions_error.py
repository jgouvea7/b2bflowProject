from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_create_contact():
    new_contact = {
        "name": "jonnathas",
        "phone": "5511999999999"
    }

    response = client.post("/v1/contacts", json=new_contact)
    assert response.status_code == 201

def test_create_contact_error():
    new_contact = {
        "name": "jonnathas",
        "phone": "5511999999999"
    }

    response = client.post("/v1/contacts", json=new_contact)
    assert response.status_code == 400


def test_delete_contact():
    phone_contact = {"phone": "5511999999999"}
    response = client.request(
        method="DELETE",
        url="/v1/contacts/delete-by-phone",
        data=json.dumps(phone_contact),
        headers={"Content-Type": "application/json"},
    )
    
    assert response.status_code == 200


def test_delete_contact_error():
    phone_contact = {"phone": "5511999999999"}
    response = client.request(
        method="DELETE",
        url="/v1/contacts/delete-by-phone",
        data=json.dumps(phone_contact),
        headers={"Content-Type": "application/json"},
    )
    
    assert response.status_code == 404



def test_delete_all_contacts_error():
    response = client.delete("/v1/contacts")
    assert response.status_code == 404


def test_delete_all_logs():
    response = client.delete("/v1/logs")
    assert response.status_code == 200


def test_delete_all_logs_error():
    response = client.delete("/v1/logs")
    assert response.status_code == 404