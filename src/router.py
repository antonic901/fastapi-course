from fastapi import APIRouter, Depends

from src.auth.dependencies import validate_token
from src.item.router import router as item_router

router = APIRouter(dependencies=[Depends(validate_token)])

router.include_router(item_router, prefix="/items", tags=["items"])
