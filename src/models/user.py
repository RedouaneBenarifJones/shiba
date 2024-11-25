from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ValidationInfo,
    ValidationError,
    field_validator
)

class User(BaseModel):
    name: str = Field()
    email: EmailStr
    password: str
    
    @field_validator("password", mode="before")
    @classmethod
    def hash_password(cls, v: str) -> bytes:
        from bcrypt import hashpw, gensalt
        from os import environ
        if len(v) < 7:
            raise ValueError("password should contain more than 7 characters.")
        password = v.encode("utf-8")
        hashed_password = hashpw(password=password, salt=gensalt())
        return hashed_password

    def check_password(self, hashed_password: str) -> bool:
        from bcrypt import checkpw
        pw = self.password.encode("utf-8")
        hashpw = self.password.encode("utf-8")
        return checkpw(password=pw, hashed_password=hashpw)
        
