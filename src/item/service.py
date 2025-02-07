from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import DBItem
from .schemas import ItemCreate, ItemUpdate

from src.database import utils as db_utils


async def get(db_session: AsyncSession, item_id: int):
    db_item = await db_session.get(DBItem, item_id)
    return db_item


async def get_all(db_session: AsyncSession, offset: int = 0, limit: int = 0):
    query = select(DBItem).offset(offset).limit(limit)
    db_result = await db_session.execute(query)
    return db_result.all()


async def create(db_session: AsyncSession, item: ItemCreate):
    db_item = DBItem(**item.model_dump())

    db_session.add(db_item)
    await db_session.commit()
    await db_session.refresh(db_item)

    return db_item


async def update(db_session: AsyncSession, db_item: DBItem, data: ItemUpdate):
    db_utils.update_model_from_schema(data, db_item)

    await db_session.commit()
    await db_session.refresh(db_item)

    return db_item


async def delete(db_session: AsyncSession, db_item: DBItem):
    await db_session.delete(db_item)
    await db_session.commit()
