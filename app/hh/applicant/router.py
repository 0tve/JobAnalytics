from fastapi import APIRouter

from .vacancy.router import router as vacancy_router

router = APIRouter(prefix="/applicant")
router.include_router(vacancy_router)
