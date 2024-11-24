from typing import Any, List, Dict
from fastapi import FastAPI
from models.user import User
from models.response import APIResponse

app = FastAPI()

@app.get("/users")
def read_users() -> APIResponse[List[User]]:
    users = []
    response = APIResponse(success=True, data=users)
    return response

@app.get("/users/user/{user_id}")
def read_user(user_id: int) -> APIResponse[User]:
    user = None
    response = APIResponse(success=True, data=user)
    return response

@app.post("/users/user")
def create_user(user_id: int) -> APIResponse[User]:
    user = None
    response = APIResponse(success=True, data=user)
    return response

@app.put("/users/user/{user_id}")
def update_user(user_id: int) -> APIResponse[User]:
    user = None
    response = APIResponse(success=True, data=user)
    return response

@app.delete("/users/user/{user_id}")
def delete_user(user_id: int) -> APIResponse[User]:
    user = None
    response = APIResponse(success=True, data=user)
    return response
