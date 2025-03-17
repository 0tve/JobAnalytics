from fastapi import APIRouter

from .vacancies.router import router as vacancies_router

router = APIRouter(prefix="/public")
router.include_router(vacancies_router)