from fastapi import APIRouter

from .applicant.router import router as applicant_router
from .public.router import router as public_router

router = APIRouter(prefix="/hh")
router.include_router(applicant_router)
router.include_router(public_router)
