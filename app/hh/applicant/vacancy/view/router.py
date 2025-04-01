from fastapi import APIRouter, Depends

from .dependencies import get_service
from .schemas import PathParameters, QueryParameters, Response
from .service import Service

router = APIRouter(prefix="/view")


@router.get("/{vacancy_id}")
async def view(service: Service = Depends(get_service),
               path_parameters: PathParameters = Depends(),
               query_parameters: QueryParameters = Depends()) -> Response:
    return service.view(vacancy_id=path_parameters.vacancy_id,
                        query_parameters=query_parameters.model_dump(exclude_none=True))