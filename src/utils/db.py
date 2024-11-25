import logging
import os
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
from models.user import User
from pydantic import ValidationError

logger = logging.getLogger()

MONGODB_HOST = os.environ["MONGODB_HOST"]
MONGODB_PORT = os.environ["MONGODB_PORT"]
MONGODB_DATABASE = os.environ["MONGODB_DATABASE"]
MONGO_INITDB_ROOT_USERNAME = os.environ["MONGO_INITDB_ROOT_USERNAME"]
MONGO_INITDB_ROOT_PASSWORD = os.environ["MONGO_INITDB_ROOT_PASSWORD"]

from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    global client, db
    try:
        client = AsyncIOMotorClient(f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}")
        db = client[MONGODB_DATABASE]
        yield
        if client:
            client.close()

    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")

async def db_create_user(user: User):
    try:
        collection = db.users
        result = await collection.insert_one(user.model_dump())
        return { "user_id": str(result.inserted_id) }
    except ValidationError as e:
        raise HTTPException(status_code=500, detail=f"Pydantic error: {str(e)}")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")

async def db_read_users():
    try:
        collection = db.users
        result = collection.find()
        users = [User(**user) async for user in result]
        return users
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")
