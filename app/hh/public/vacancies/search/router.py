from fastapi import APIRouter, Depends

from .dependencies import get_service
from .schemas import QueryParameters
from .service import Service

router = APIRouter(prefix="/search")


@router.get("")
async def search(service: Service = Depends(get_service),
                query_parameters: QueryParameters = Depends()):
    return await service.search(query_parameters=query_parameters.model_dump(exclude_none=True))