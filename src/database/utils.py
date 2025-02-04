from pydantic import BaseModel

from .models import DBBase


def calculate_offset(page: int = 1, limit: int = 10):
    return (page - 1) * limit


def update_model_from_schema(schema: BaseModel, db_model: DBBase):
    for field, value in schema.model_dump(exclude_unset=True).items():
        if hasattr(db_model, field):
            setattr(db_model, field, value)
    return db_model
