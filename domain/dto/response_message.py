from pydantic import BaseModel
from typing import Optional

class ResponseMessage(BaseModel):
    message: Optional[str] = None