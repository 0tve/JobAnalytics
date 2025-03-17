from fastapi import APIRouter, Depends, Query

from app.hh.public.vacancies.search.schemas import QueryParameters as SearchQueryParameters

from .dependencies import get_service
from .service import Service

router = APIRouter(prefix="/collect")


@router.get("")
async def collect(service: Service = Depends(get_service),
                  limit: int = Query(default=2000, ge=1, le=2000),
                  search_query_parameters: SearchQueryParameters = Depends()):
    return await service.collect(limit=limit, search_query_parameters=search_query_parameters)