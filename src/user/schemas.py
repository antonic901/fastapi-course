from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict

from src.auth.enums import UserRole


class UserProfileBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    role: UserRole
    first_name: str
    last_name: str


class UserProfile(UserProfileBase):
    id: str


class UserProfileCreate(UserProfile):
    pass


class UserProfileRead(UserProfileBase):
    id: str
    created_at: datetime
    updated_at: datetime


class UserProfileUpdate(UserProfileBase):
    role: UserRole | None = None
    first_name: str | None = None
    last_name: str | None = None
