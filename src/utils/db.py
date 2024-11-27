import logging
import os
from typing import AsyncGenerator
from bson.errors import InvalidId
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
from models.user import User
from pydantic import ValidationError
from bson import ObjectId

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
        user_document = user.hash_password().model_dump()
        result = await collection.insert_one(user_document)
        return { "user_id": str(result.inserted_id) }
    except ValidationError as e:
        raise HTTPException(status_code=500, detail=f"Pydantic error: {str(e)}")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")

async def db_read_user(id: str):
    try:
        collection = db.users
        result = await collection.find_one({ "_id": ObjectId(id) })
        if result is None:
            raise HTTPException(status_code=404, detail="User not found.")
        user = User(**result)
        return user
    except InvalidId as e:
            raise HTTPException(status_code=400, detail="Invalid id.")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")

async def db_read_users():
    try:
        collection = db.users
        result = collection.find()
        users = [User.from_document(user) async for user in result]
        return users
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")
