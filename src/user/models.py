from sqlalchemy.orm import Mapped, mapped_column

from src.auth.enums import UserRole
from src.database.models import DBBase


class DBUserProfile(DBBase):
    __tablename__ = "userprofiles"

    id: Mapped[str] = mapped_column(primary_key=True)
    role: Mapped[UserRole]
    first_name: Mapped[str]
    last_name: Mapped[str]
