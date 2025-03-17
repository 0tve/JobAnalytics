from fastapi import APIRouter

from .vacancies.router import router as vacancies_router

router = APIRouter(prefix="/features")
router.include_router(vacancies_router)
