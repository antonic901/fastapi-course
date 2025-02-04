from sqlalchemy.orm import DeclarativeBase

from .mixins import TimeStampMixin


class DBBase(TimeStampMixin, DeclarativeBase):
    pass
