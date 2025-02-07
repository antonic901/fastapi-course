from http import HTTPStatus

from fastapi import HTTPException


class ItemNotFound(HTTPException):
    def __init__(self, headers=None):
        super().__init__(HTTPStatus.NOT_FOUND, "Item not found", headers)
