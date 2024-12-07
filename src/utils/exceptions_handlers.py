import logging
from src.main import app
from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import ValidationError
from pymongo.errors import PyMongoError
from models.responses import APIFailureResponse
from fastapi.encoders import jsonable_encoder


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exception: ValidationError):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            type=ValidationError.__name__,
            details=repr(exception),
            traceback=None,
        ).model_dump()
    )


@app.exception_handler(RequestValidationError)
async def request_exception_handler(
    request: Request, exception: RequestValidationError
):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            type=RequestValidationError.__name__,
            details=repr(exception),
            traceback=None,
        ).model_dump()
    )


@app.exception_handler(PyMongoError)
async def mongo_db_exception_handler(request: Request, exception: PyMongoError):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            type=PyMongoError.__name__,
            details=repr(exception),
            traceback=None,
        ).model_dump()
    )
