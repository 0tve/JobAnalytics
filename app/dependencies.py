from fastapi import Depends
from httpx import AsyncClient

from app.app_state import get_http_client, get_rps_limiter
from app.rps_limiter import RPSLimiter
from app.services import VacancySearchService, VacancyService


def get_vacancy_search_service(http_client: AsyncClient = Depends(get_http_client),
                               rps_limiter: RPSLimiter = Depends(get_rps_limiter)) -> VacancySearchService:
    return VacancySearchService(http_client, rps_limiter)

def get_vacancy_service(http_client: AsyncClient = Depends(get_http_client),
                        rps_limiter: RPSLimiter = Depends(get_rps_limiter),
                        vacancy_search_service: VacancySearchService = Depends(get_vacancy_search_service)) -> VacancyService:
    return VacancyService(http_client, rps_limiter, vacancy_search_service)
