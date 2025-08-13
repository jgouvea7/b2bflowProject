from fastapi import APIRouter
from services.logs_service import *


logs = APIRouter()

@logs.get("/v1/logs")
def get_logs_api():
    return get_logs()

@logs.delete("/v1/logs")
def delete_logs_api():
    return delete_logs()
