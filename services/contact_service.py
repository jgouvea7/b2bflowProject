from infrastructure.model.contact import session, ContactModel
from domain.dto.create_contact import CreateContact
from fastapi import HTTPException, status
from services.logs_service import create_log
from dotenv import load_dotenv
import requests
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

        document = {
            "name": new_user.name,
            "phone": new_user.phone
        }

        create_log(document, "contact-create-success")
        session.add(new_user)
        session.commit()



def get_contacts():
    try:
        contacts = session.query(ContactModel).all()
        return contacts
    finally:
        session.close()


def get_contact_by_phone(phone: str):
    contact = session.query(ContactModel).filter(ContactModel.phone == phone).first()
    if contact:
        return contact
 


def delete_contacts():
    contacts = session.query(ContactModel).all()
    with session:
        for contact in contacts:
            session.delete(contact)
        session.commit()

        document = {
        "status": "success",
        "message": "Contacts were successfully deleted"
    }
        create_log(document, "contact-delete-all-success")
    return document



def delete_contact_by_phone(phone: str):
    contact = get_contact_by_phone(phone)
    if contact:
        with session:
            session.delete(contact)
            session.commit()

            document = {
                "status": "success",
                "message": f"Contact '{contact.name}' with number  {contact.phone} was successfully deleted"
            }
            create_log(document, "contact-delete-success")
            return document
    else:
        document = {
            "status": "error",
            "error": "Contact not found"
        }
        create_log(document, "contact-delete-error")
        return  document



def send_message_all():
    try:
        contacts = get_contacts()
        if contacts:
            results = []

            for contact in contacts:
                url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

                payload = {
                    "phone": contact.phone,
                    "message": f"Olá {contact.name}, tudo bem com você?"
                }

                headers = {
                    "Content-type": "application/json",
                    "client-token": CLIENT_TOKEN
                }

                response = requests.post(url, json=payload, headers=headers)

                if response.status_code == 200:
                    document = {
                        "phone": contact.phone,
                        "status": "success",
                        "message": "Message sent successfully"
                    }

                    results.append(document)
                    create_log(document, "message-send-success")
                else:
                    document = {
                        "phone": contact.phone,
                        "status": "error",
                        "error": f"Failed to send message: {response.text}"
                    }

                    results.append(document)
                    create_log(document, "message-send-error")
            return results
        else:
            return {
                "status": "error",
                "error": "No contacts found"
            }
    except Exception as e:
        document = {"error": f"Unexpected error occurred: {e}"}
        create_log(document, "unexpected-error")
        return document






