from typing import List, Optional, Annotated
from fastapi import FastAPI, Request, Query
from models.user import User
from models.response import APISuccessResponse
from dotenv import load_dotenv
from utils.db import db_read_user, db_read_users, db_create_user, lifespan
import logging
import os

load_dotenv()

app = FastAPI(lifespan=lifespan)
logger = logging.getLogger(__name__)

# importing all the exception handlers to register them first
import utils.exceptions_handlers

# route handlers
@app.get("/users")
async def read_users(
        page: int = Query(default=1, ge=1, title="page number"), 
        page_size: int = Query(default=3, ge=1, title="page size")
) -> Optional[APISuccessResponse[List[User]]]:
    users = await db_read_users(page=page, page_size=page_size)
    if users:
        return APISuccessResponse[List[User]](
            data=users,
            count=len(users),
            previous=f"{os.environ["API_URL"]}/users?page={page - 1}&page_size={page_size}" if page > 1 else None,
            next=f"{os.environ["API_URL"]}/users?page={page + 1}&page_size={page_size}" if len(users) > page_size - 1 else None,
        )

@app.get("/users/user/{user_id}")
async def read_user(user_id: str) -> APISuccessResponse[User]:
    user = await db_read_user(user_id)
    return APISuccessResponse[User](data=user)

@app.post("/users/user")
async def create_user(request: Request):
    user_document = await request.json()
    response = await db_create_user(User(**user_document))
    user = await db_read_user(response["user_id"])
    return APISuccessResponse[User](data=user)

@app.put("/users/user/{user_id}")
def update_user(user_id: str):
    pass

@app.delete("/users/user/{user_id}")
def delete_user(user_id: str):
    pass
