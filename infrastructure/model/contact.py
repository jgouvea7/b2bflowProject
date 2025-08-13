from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from infrastructure.db.db import *
import uuid

Base = declarative_base()

class ContactModel(Base):
    __tablename__ = "contacts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)