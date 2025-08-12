from fastapi import FastAPI
from sqlalchemy import create_engine
from dotenv import load_dotenv
from api.controller import router
import os

load_dotenv(dotenv_path="../b2bflow/infrastructure/env/supabase.env")

URL_DB = os.getenv("DB")

app = FastAPI()
app.include_router(router)
engine = create_engine(URL_DB)
