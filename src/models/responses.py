from typing import Any, Optional
from pydantic import BaseModel


class APISuccessResponse[Data](BaseModel):
    status_code: Optional[int] = None
    count: Optional[int] = None
    previous: Optional[str] = None
    next: Optional[str] = None
    data: Optional[Data] = None


class APIFailureResponse(BaseModel):
    status_code: Optional[int]
    type: Optional[str]
    details: Optional[str]
    traceback: Optional[Any]
