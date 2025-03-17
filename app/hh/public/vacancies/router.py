from fastapi import APIRouter

from .search.router import router as search_router


router = APIRouter(prefix="/vacancies")
router.include_router(search_router)