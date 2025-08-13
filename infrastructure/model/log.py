from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from infrastructure.db.db import *
import uuid

Base = declarative_base()

class LogModel(Base):
    __tablename__ = "logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    document = Column(JSON, nullable = False)
    log_type = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    


Base.metadata.create_all(bind=engine)