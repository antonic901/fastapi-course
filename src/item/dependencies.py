from typing import Annotated

from fastapi import Depends

from .models import DBItem
from .service import get
from .exceptions import ItemNotFound

from src.database.core_async import DbAsyncSession


async def valid_item_id(db_session: DbAsyncSession, item_id: int):
    item = await get(db_session, item_id)
    if not item:
        raise ItemNotFound()
    return item


ValidItem = Annotated[DBItem, Depends(valid_item_id)]
