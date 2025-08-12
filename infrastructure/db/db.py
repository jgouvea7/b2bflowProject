from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../b2bflow/infrastructure/env/supabase.env")

supabase_url = os.getenv("SUPABASE_URL")
superbase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, superbase_key)