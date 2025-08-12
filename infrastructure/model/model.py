from sqlalchemy import create_engine, Column, String, UUID
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

Base = declarative_base()
load_dotenv(dotenv_path="../b2bflow/infrastructure/env/supabase.env")
supabase_db = os.getenv("DATABASE_URL")

engine = create_engine(supabase_db)
session_config = sessionmaker(bind=engine)

session = session_config()


class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    cell = Column(String, nullable=False)
