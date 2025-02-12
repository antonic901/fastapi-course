from typing import Annotated
from functools import lru_cache

from fastapi import Depends
from permit import Permit

from .exceptions import Unauthorized

from src.config import get_settings

settings = get_settings()


class Authorization(Permit):
    def __init__(self, config=None, **options):
        super().__init__(config, **options)

    async def check(self, user_id: str, action: str, resource, context=None):
        """
        Checks if the user with the given ID has permission to execute the specified action on the given resource.
        """
        permitted = await super().check(user_id, action, resource, context)
        if not permitted:
            raise Unauthorized(
                f"User is NOT PERMITTED to perfom action: {action} on resource: {resource}!"
            )


@lru_cache()
def get_authorization() -> Authorization:
    return Authorization(pdp=settings.permit_api_url, token=settings.permit_token)


Authorization = Annotated[Authorization, Depends(get_authorization)]
