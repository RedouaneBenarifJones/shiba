from datetime import datetime, timezone
from typing import Optional, Any, Self
from bson import ObjectId
from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    field_validator,
    ValidationError
)
import logging


logger = logging.getLogger()

class User(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("id", mode="before")
    @classmethod
    def validate_id(cls, v: ObjectId) -> str:
        return str(v)

    def hash_password(self) -> Self:
        from bcrypt import hashpw, gensalt
        hashed_password = hashpw(self.password.encode('utf-8'), gensalt()).decode('utf-8')
        self.password = hashed_password
        return self

    def check_password(self, hashed_password: str) -> bool:
        from bcrypt import checkpw
        pw = self.password.encode("utf-8")
        hashpw = hashed_password.encode("utf-8")
        return checkpw(password=pw, hashed_password=hashpw)

    @classmethod
    def from_document(cls, document) -> Self:
        """Convert MongoDB document to Pydantic model."""
        try:
            if "_id" in document:
                document["_id"] = str(document["_id"])
            return cls(**document)
        except ValidationError as e:
            logger.error(e.errors())
            raise e

    def __setattr__(self, name: str, value: Any) -> None:
        if name != "updated_at":
            self.updated_at = datetime.now(timezone.utc)
        super().__setattr__(name, value)
