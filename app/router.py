from fastapi import APIRouter, Depends, Query

from app.dependencies import get_vacancy_search_service, get_vacancy_service
from app.schemas import (Vacancy, VacancyParams, VacancySearch,
                         VacancySearchParams)
from app.services import VacancySearchService, VacancyService

router = APIRouter()

@router.post("/vacancies")
async def collect_vacancies(vacancy_service: VacancyService = Depends(get_vacancy_service),
                            limit: int = Query(default=2000, ge=1, le=2000),
                            vacancy_search_params: VacancySearchParams = Depends()) -> list[Vacancy]:
    return await vacancy_service.collect_vacancies(limit, vacancy_search_params.model_dump(exclude_none=True))

@router.post("/vacancies/{vacancy_id}")
async def collect_vacancy(vacancy_id: str,
                          vacancy_service: VacancyService = Depends(get_vacancy_service),
                          vacancy_params: VacancyParams = Depends()) -> Vacancy:
    return await vacancy_service.collect_vacancy(vacancy_id, vacancy_params.model_dump(exclude_none=True))

@router.get("/vacancies/{vacancy_id}")
async def view(vacancy_id: str,
               vacancy_service: VacancyService = Depends(get_vacancy_service),
               vacancy_params: VacancyParams = Depends()) -> Vacancy:
    return await vacancy_service.view_vacancy(vacancy_id, vacancy_params.model_dump(exclude_none=True))

@router.get("/vacancy_searches")
async def search(vacancy_search_service: VacancySearchService = Depends(get_vacancy_search_service),
                 vacancy_search_params: VacancySearchParams = Depends()) -> VacancySearch:
    return await vacancy_search_service.search_vacancies(vacancy_search_params.model_dump(exclude_none=True))