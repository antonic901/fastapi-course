from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import DBBase


class DBItem(DBBase):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    icon: Mapped[str]
    title: Mapped[str]
    description: Mapped[str]
    creator_id: Mapped[str] = mapped_column(ForeignKey("userprofiles.id"))
