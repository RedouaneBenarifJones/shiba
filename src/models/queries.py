from pydantic import BaseModel, Field
from typing import Literal


class UsersQueryParams(BaseModel):
    page: int = Field(default=1, ge=1, title="page number")
    page_size: int = Field(default=3, ge=1, title="page size")
    order_by: Literal["created_at", "updated_at", "name", "email"] = "created_at"

    model_config = {"extra": "forbid"}
