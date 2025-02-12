from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class UserProfileBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

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
    first_name: str | None = None
    last_name: str | None = None
