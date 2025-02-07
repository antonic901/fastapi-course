from datetime import datetime

from pydantic import Field, BaseModel
from pydantic import ConfigDict


class ItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    icon: str
    title: str = Field(max_length=128)
    description: str


class Item(ItemBase):
    id: int | None = Field(default=None)


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ItemUpdate(ItemBase):
    icon: str | None = None
    title: str | None = None
    description: str | None = None
