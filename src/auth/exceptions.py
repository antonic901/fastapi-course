from http import HTTPStatus

from fastapi import HTTPException


class AuthException(HTTPException):
    def __init__(self, headers=None):
        super().__init__(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            "Error with authentication service",
            headers,
        )


class Unauthorized(HTTPException):
    def __init__(self, message="Unauthorized", headers=None):
        super().__init__(HTTPStatus.UNAUTHORIZED, message, headers)
