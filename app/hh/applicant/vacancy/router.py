from fastapi import APIRouter
from .view.router import router as view_router

router = APIRouter(prefix="/vacancy")
router.include_router(view_router)