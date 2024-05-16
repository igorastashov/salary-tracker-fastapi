from fastapi import HTTPException
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
)


class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail="User not found")


class IncorrectCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTP_400_BAD_REQUEST, detail="Incorrect username or password"
        )


class UserAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTP_400_BAD_REQUEST,
            detail="User with this email already exists!",
        )


class UnauthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED")


class ExpiredTokenException(HTTPException):
    def __init__(self):
        super().__init__(status_code=HTTP_401_UNAUTHORIZED, detail="Token has expired")
