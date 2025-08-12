from pydantic import BaseModel

class CreateContact(BaseModel):
    name: str
    phone: str