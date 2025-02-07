from fastapi import APIRouter

from src.item.router import router as item_router

router = APIRouter()

router.include_router(item_router, prefix="/items", tags=["items"])
