from fastapi import APIRouter

from .collect.router import router as collect_router

router = APIRouter(prefix="/vacancies")
router.include_router(collect_router)