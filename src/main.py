import logging
from typing import Any, List, Dict, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from models.user import User
from models.response import APIResponse
from dotenv import load_dotenv
from utils.db import db_read_user, db_read_users, db_create_user, lifespan

load_dotenv()
app = FastAPI(lifespan=lifespan)
logger = logging.getLogger(__name__)

@app.get("/users")
async def read_users() -> Any:
    try:
        users = await db_read_users()
        return APIResponse(success=True, data=users)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})

@app.get("/users/user/{user_id}")
async def read_user(user_id: str) -> APIResponse[User]:
    user = await db_read_user(user_id)
    response = APIResponse(success=True, data=user)
    return response

@app.post(
    "/users/user",
    response_model=APIResponse[User]
)
async def create_user(request: Request):
    try:
        user_document = await request.json()
        response = await db_create_user(User(**user_document))
        user = await db_read_user(response["user_id"])
        return APIResponse(success=True, data=user)
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors())
    except HTTPException as e:
        return HTTPException(status_code=e.status_code, detail=e.detail)


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
