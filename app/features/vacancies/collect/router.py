from fastapi import APIRouter, Depends, Query

from app.hh.public.vacancies.search.router import search

from .dependencies import get_service
from .service import Service

router = APIRouter(prefix="/collect")


@router.get("")
async def collect(service: Service = Depends(get_service),
                  limit: int = Query(default=2000, ge=1, le=2000),
                  search_result: dict = Depends(search)):
    return await service.collect(search_result=search_result, limit=limit)