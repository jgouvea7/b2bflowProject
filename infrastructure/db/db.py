from sqlalchemy.orm import sessionmaker
from supabase import create_client
from dotenv import load_dotenv
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../b2bflow/infrastructure/env/supabase.env")

supabase_client = os.getenv("DATABASE_CLIENT")
engine = create_engine(supabase_client)
session_config = sessionmaker(bind=engine)

session = session_config()
supabase_url = os.getenv("SUPABASE_URL")
superbase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, superbase_key)

