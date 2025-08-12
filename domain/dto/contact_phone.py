from pydantic import BaseModel

class ContactPhone(BaseModel):
    phone: str