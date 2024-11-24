from typing import Optional
from pydantic import BaseModel
from fastapi import status


class APIResponse[T](BaseModel):
    success: bool
    status_code: Optional[int] = status.HTTP_200_OK
    message: Optional[str] = None
    data: Optional[T] = None
