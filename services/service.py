from infrastructure.model.model import session, ContactModel
from fastapi import HTTPException, status
from domain.dto.create_contact import CreateContact
import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../b2bflow/infrastructure/env/z-api.env")
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")
INSTANCE_ID = os.getenv("INSTANCE_ID")
TOKEN = os.getenv("TOKEN")


def create_contact(contact: CreateContact):
    user_existing = session.query(ContactModel).filter(ContactModel.phone == contact.phone).first()
    if user_existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone already registered"
            )
    
    with session:
        new_user = ContactModel(
            name=contact.name,
            phone=contact.phone
        )
        session.add(new_user)
        session.commit()



def get_contacts():
    try:
        contacts = session.query(ContactModel).all()
        return contacts
    finally:
        session.close()



def get_contact_by_phone(phone: str):
    try:
        contact = session.query(ContactModel).filter(ContactModel.phone == phone).first()
        return contact
    finally:
        session.close()



def delete_contacts():
    contacts = session.query(ContactModel).all()
    with session:
        for contact in contacts:
            session.delete(contact)
        session.commit()
    
    return {
        "message": "Contacts were successfully deleted"
    }



def delete_contact_by_phone(phone: str):
    contact = get_contact_by_phone(phone)
    with session:
        if contact:
            session.delete(contact)
            session.commit()

            return {
                "message": f"Contact '{contact.name}' with number  {contact.phone} was successfully deleted"
            }
        else:
            return {
                "message": "Contact not found"
            }



def send_message(phone: str):
    try:
        contact = get_contact_by_phone(phone)
        if contact:
            url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

            payload = {
                "phone": phone,
                "message": f"Olá {contact.name}, tudo bem com você?"
            }

            headers = {
                "Content-type": "application/json",
                "client-token": CLIENT_TOKEN
            }

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                return {
                    "message": "Message sent successfully"
                }
            else:
                return {
                    "error": f"Failed to send message: {response.text}"
                }
        else:
            return {"error": "Contact not found"}
    except Exception as e:
        return {
            "error": f"Unexpected error occurred: {e}"
        }