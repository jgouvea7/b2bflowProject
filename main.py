from fastapi import FastAPI
from sqlalchemy import create_engine
from infrastructure.db.db import supabase
from api.controller import router

app = FastAPI()
app.include_router(router)
engine = create_engine(supabase)
