from httpx import AsyncClient, HTTPError
from sqlalchemy.exc import SQLAlchemyError

from app.config import HHSettings
from app.db import async_session_maker
from app.repository import vacancy_insert
from app.rps_limiter import RPSLimiter
from app.schemas import Vacancy, VacancyParams, VacancySearchHeaders

hh = HHSettings()


class VacancyService:
    
    def __init__(self,
                 http_client: AsyncClient,
                 rps_limiter: RPSLimiter,
                 vacancy_search_service: "VacancySearchService") -> None:
        self.http_client = http_client
        self.rps_limiter = rps_limiter
        self.vacancy_search_service = vacancy_search_service
        
    async def collect_pages(self, limit: int, vacancy_search_params: dict):
        pages = []
        per_page = vacancy_search_params["per_page"]
        vacancy_search_params["per_page"] = min(limit, per_page)
        vacancy_search = await self.vacancy_search_service.search_vacancies(vacancy_search_params)
        found = vacancy_search["found"]
        vacancies_to_collect = min(found, limit)
        pages_to_collect = -(-vacancies_to_collect // per_page)
        
        for page in range(pages_to_collect):
            vacancy_search_params["page"] = page
            vacancy_search = await self.vacancy_search_service.search_vacancies(vacancy_search_params)
            pages.append(vacancy_search)
            
        return pages
    
    def get_vacancy_ids(self, limit: int, pages: list[dict]):
        vacancy_ids = []
        
        for page in pages:
            vacancy_ids.extend([vacancy["id"] for vacancy in page["items"]])
                      
        return vacancy_ids[:limit]
        
    async def collect_vacancies(self, limit: int, vacancy_search_params: dict):
        vacancy_schemas = []
        vacancy_params = VacancyParams(locale=vacancy_search_params["locale"],
                                       host=vacancy_search_params["host"]).model_dump(exclude_none=True)
        pages = await self.collect_pages(limit=limit, vacancy_search_params=vacancy_search_params)
        vacancy_ids = self.get_vacancy_ids(limit=limit, pages=pages)
        
        for vacancy_id in vacancy_ids:
            
            try:
                vacancy = await self.view_vacancy(vacancy_id, vacancy_params)
                vacancy_schemas.append(Vacancy(**vacancy))
                
            except HTTPError as e:
                print(f"HTTP ERROR!!!\n\n{e}\n\nHTTP ERROR!!!")
                break
            
            async with async_session_maker() as session:
                
                try:
                    await vacancy_insert(session, vacancy)
                    await session.commit()
                    
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
 
        return vacancy_schemas
    
    async def view_vacancy(self, vacancy_id: str, vacancy_params: dict):
        response = await self.rps_limiter.request(self.http_client.get,
                                                  f"{hh.VACANCIES_URL}/{vacancy_id}",
                                                  params=vacancy_params)
        response.raise_for_status()
        return response.json()
    
    async def collect_vacancy(self, vacancy_id: str, vacancy_params: dict):
        vacancy = await self.view_vacancy(vacancy_id, vacancy_params)
        vacancy_schema = Vacancy(**vacancy)

        async with async_session_maker() as session:
            
            try:
                await vacancy_insert(session, vacancy)
                await session.commit()
                
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            
        return vacancy_schema
    

class VacancySearchService:
    
    def __init__(self, http_client: AsyncClient, rps_limiter: RPSLimiter) -> None:
        self.http_client = http_client
        self.rps_limiter = rps_limiter
        
    async def search_vacancies(self, vacancy_search_params: dict):
        vacancy_search_headers = VacancySearchHeaders().model_dump()
        response = await self.rps_limiter.request(self.http_client.get,
                                                  f"{hh.VACANCIES_URL}",
                                                  params=vacancy_search_params,
                                                  headers=vacancy_search_headers)
        response.raise_for_status()
        return response.json()
