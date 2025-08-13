from fastapi import APIRouter, HTTPException
from domain.dto.contact_response import ContactResponse
from domain.dto.create_contact import CreateContact
from domain.dto.contact_phone import ContactPhone
from domain.dto.response_message import ResponseMessage
from services.service import *


router = APIRouter()


@router.post("/v1/contacts", status_code=status.HTTP_201_CREATED)
def create_contact_api(contact: CreateContact):
    create_contact(contact)
    return {
        "message": "Contact created successfully"
    }


@router.get("/v1/contacts", response_model=list[ContactResponse])
def get_contacts_api():
    return get_contacts()



@router.get("/v1/contacts/get-by-phone", response_model=ContactResponse)
def get_contact_by_phone_api(contact: ContactPhone):
    contact = get_contact_by_phone(contact.phone)
    return {
         "name": contact.name,
         "phone": contact.phone
    }



@router.post("/v1/contacts/send-message")
def send_message_api(contact: ContactPhone):
    result = send_message(contact.phone)
    return result


@router.post("/v1/contacts/send-message-all")
def send_message_all_api():
    return send_message_all()


@router.delete("/v1/contacts")
def delete_contact_api():
    result = delete_contacts()
    return result



@router.delete("/v1/contacts/delete-by-phone", response_model=ResponseMessage)
def delete_contact_by_phone_api(contact: ContactPhone):
    result = delete_contact_by_phone(contact.phone)
    return result