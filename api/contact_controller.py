from fastapi import APIRouter
from domain.dto.contact_response import ContactResponse
from domain.dto.create_contact import CreateContact
from domain.dto.contact_phone import ContactPhone
from services.contact_service import *


contact = APIRouter()


@contact.post("/v1/contacts", status_code=status.HTTP_201_CREATED)
def create_contact_api(contact: CreateContact):
    create_contact(contact)
    return {
        "status": "success",
        "message": "Contact created successfully"
    }


@contact.get("/v1/contacts", response_model=list[ContactResponse])
def get_contacts_api():
    return get_contacts()



@contact.get("/v1/contacts/get-by-phone")
def get_contact_by_phone_api(contact: ContactPhone):
    contact = get_contact_by_phone(contact.phone)
    if contact:
        return contact
    else:
        return {
            "status": "error",
            "error": "Contact not found"
        }


@contact.post("/v1/contacts/send-message-all")
def send_message_all_api():
    return send_message_all()


@contact.delete("/v1/contacts")
def delete_contact_api():
    return delete_contacts()



@contact.delete("/v1/contacts/delete-by-phone")
def delete_contact_by_phone_api(contact: ContactPhone):
    result = delete_contact_by_phone(contact.phone)
    return result

