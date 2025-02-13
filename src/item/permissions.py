from fastapi import Request

from .dependencies import valid_item_id

from src.auth.core import Authorization
from src.auth.dependencies import UserProfile
from src.auth.utils import get_action_from_method
from src.database.core_async import DbAsyncSession


async def crud_permission(
    request: Request,
    auth: Authorization,
    db_session: DbAsyncSession,
    db_userprofile: UserProfile,
    item_id: int | None = None,
):
    """
    Check if the given user has the necessary permissions to perform an CRUD action on an item.

    If `item_id` is provided, it checks whether the user is the creator of the specified item.
    """
    resource = {"type": "items"}

    if item_id:
        db_item = await valid_item_id(db_session, item_id)
        resource["attributes"] = {"creator_id": db_item.creator_id}

    await auth.check(
        db_userprofile.id, get_action_from_method(request.method), resource
    )
