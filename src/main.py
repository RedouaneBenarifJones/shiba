from typing import List, Optional, Annotated
from fastapi import FastAPI, Request, Query
from starlette.status import HTTP_200_OK
from models.user import User
from models.responses import APISuccessResponse
from dotenv import load_dotenv
from utils.db import db_read_user, db_read_users, db_create_user, lifespan
import logging
import os
from models.queries import UsersQueryParams

load_dotenv()

app = FastAPI(lifespan=lifespan)
logger = logging.getLogger(__name__)

# importing all the exception handlers to register them first
import utils.exceptions_handlers


@app.get("/health", status_code=200)
def health():
    return {"status": "healthy"}


@app.get("/users")
async def read_users(
    filters: Annotated[UsersQueryParams, Query()],
) -> Optional[APISuccessResponse[List[User]]]:
    page = filters.page
    page_size = filters.page_size
    users = await db_read_users(filters)
    if users:
        return APISuccessResponse[List[User]](
            status_code=HTTP_200_OK,
            data=users[:page_size],
            count=len(users) - 1 if len(users) > page_size else len(users),
            previous=f"/users?page={page - 1}&page_size={page_size}"
            if page > 1
            else None,
            next=f"{os.environ["HOSTNAME"]}/users?page={page + 1}&page_size={page_size}"
            if len(users) > page_size
            else None,
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
