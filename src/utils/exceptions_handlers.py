from src.main import app
from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from pymongo.errors import PyMongoError
from models.response import APIFailureResponse
import traceback

# exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            type=HTTPException.__name__,
            details= repr(exception),
            traceback=None
        ).model_dump()
    )

@app.exception_handler(ValueError)
async def value_exception_handler(request: Request, exception: ValueError):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            type=ValueError.__name__,
            details= repr(exception),
            traceback=traceback.format_exc()
        ).model_dump()
    )

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exception: ValidationError):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            type=ValidationError.__name__,
            details= repr(exception),
            traceback=None
        ).model_dump()
    )

@app.exception_handler(RequestValidationError)
async def request_exception_handler(request: Request, exception: RequestValidationError):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            type=RequestValidationError.__name__,
            details=repr(exception),
            traceback=None
        ).model_dump()
    )

@app.exception_handler(PyMongoError)
async def mongo_db_exception_handler(request: Request, exception: PyMongoError):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            type=PyMongoError.__name__,
            details= repr(exception),
            traceback=None
        ).model_dump()
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        content=APIFailureResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            type=HTTPException.__name__,
            details= repr(exception),
            traceback=None
        ).model_dump()
    )

