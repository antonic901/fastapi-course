from typing import Annotated
from http import HTTPStatus

from fastapi import APIRouter, Query

from .schemas import ItemRead, ItemCreate, ItemUpdate
from .service import get_all, create, update, delete
from .dependencies import ValidItem

from src.database.core_async import DbAsyncSession
from src.database.dependencies import DbOffset

router = APIRouter()


@router.get("", response_model=list[ItemRead])
async def get_items(
    db_session: DbAsyncSession,
    offset: DbOffset,
    limit: Annotated[int, Query(ge=10, le=100)] = 10,
):
    db_items = await get_all(db_session, offset, limit)
    return [ItemRead.model_validate(db_row[0]) for db_row in db_items]


@router.get("/{item_id}", response_model=ItemRead)
async def get_item(db_item: ValidItem):
    return ItemRead.model_validate(db_item)


@router.post("", response_model=ItemRead, status_code=HTTPStatus.CREATED)
async def create_item(db_session: DbAsyncSession, item: ItemCreate):
    db_item = await create(db_session, item)
    return ItemRead.model_validate(db_item)


@router.patch("/{item_id}")
async def update_item(db_session: DbAsyncSession, db_item: ValidItem, data: ItemUpdate):
    await update(db_session, db_item, data)
    return ItemRead.model_validate(db_item)


@router.delete("/{item_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_item(db_session: DbAsyncSession, db_item: ValidItem):
    await delete(db_session, db_item)
