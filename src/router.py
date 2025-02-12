from fastapi import APIRouter, Depends

from src.auth.permissions import crud_permission

from src.item.router import router as item_router

router = APIRouter(dependencies=[Depends(crud_permission)])

router.include_router(item_router, prefix="/items", tags=["items"])
