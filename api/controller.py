from fastapi import APIRouter, HTTPException
from domain.dto.contact_response import ContactResponse
from domain.dto.create_contact import CreateContact
from domain.dto.contact_phone import ContactPhone
from domain.dto.response_message import ResponseMessage
from services.service import *


router = APIRouter()


@router.post("/v1/contacts")
def create_contact_api(contact: CreateContact):
    create_contact(contact)
    return {
        "message": "Create contact is succefully"
    }


@router.get("/v1/contacts", response_model=list[ContactResponse])
def get_contacts_api():
    return get_contacts()



@router.get("/v1/contacts/by-phone", response_model=ContactResponse)
def get_contact_by_phone_api(contact: ContactPhone):
    contact = get_contact_by_phone(contact.phone)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {
         "name": contact.name,
         "phone": contact.phone
    }



@router.post("/v1/contacts/send-message", response_model=ResponseMessage)
def send_message_api(contact: ContactPhone):
    result = send_message(contact.phone)
    return result



@router.delete("/v1/contacts")
def delete_contact_api():
    result = delete_contacts()
    return result



@router.delete("/v1/contacts/by-phone")
def delete_contact_by_phone_api(contact: ContactPhone):
    result = delete_contact_by_phone(contact.phone)
    return result