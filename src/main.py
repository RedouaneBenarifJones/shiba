from typing import Any, List, Dict, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models.user import User
from models.response import APIResponse
from dotenv import load_dotenv
from utils.db import db_read_users, db_create_user, lifespan

load_dotenv()
app = FastAPI(lifespan=lifespan)

@app.get("/users")
async def read_users() -> Any:
    try:
        users = await db_read_users()
        return users
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})

@app.get("/users/user/{user_id}")
async def read_user(user_id: int) -> APIResponse[User]:
    user = None
    response = APIResponse(success=True, data=user)
    return response

@app.post("/users/user/{username}/{email}/{password}")
async def create_user(username: str, email: str, password: str):
    try:
        user = await db_create_user(User(name=username, email=email, password=password))
        return user
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})


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
