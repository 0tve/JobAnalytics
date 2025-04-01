from httpx import AsyncClient

from app.core.config import AppSettings
from app.hh.applicant.vacancy.view.schemas import \
    QueryParameters as ViewQueryParameters
from app.hh.rps_limiter import RPSLimiter

from .repository import Repository

app_settings = AppSettings()


class Service:
    
    def __init__(self, repo: Repository, http_client: AsyncClient):
        self.repo = repo
        self.rps_limiter = RPSLimiter()
        self.http_client = http_client
    
    async def collect_pages(self, limit: int, search_query_parameters: dict):
        pages = []
        response = await self.rps_limiter.request(self.http_client.get, app_settings.SEARCH_URL, follow_redirects=True, params=search_query_parameters)
        response.raise_for_status()
        search_result = response.json()
        per_page = search_result["per_page"]
        found = search_result["found"]
        vacancies_to_collect = min(found, limit)
        pages_to_collect = -(-vacancies_to_collect // per_page)
        
        for page in range(pages_to_collect):
            search_query_parameters["page"] = page
            response = await self.rps_limiter.request(self.http_client.get, app_settings.SEARCH_URL, follow_redirects=True, params=search_query_parameters)
            response.raise_for_status()
            result = response.json()
            pages.append(result)
            
        return pages
    
    def get_vacancy_ids(self, limit: int, pages: list[dict]):
        vacancy_ids = []
        
        for page in pages:
            vacancy_ids.extend([vacancy["id"] for vacancy in page["items"]])
                      
        return vacancy_ids[:limit]
    
    async def collect(self, limit: int, search_query_parameters: dict):
        vacancies = []
        view_query_parameters = ViewQueryParameters(locale=search_query_parameters["locale"], host=search_query_parameters["host"]).model_dump(exclude_none=True)
        pages = await self.collect_pages(limit=limit, search_query_parameters=search_query_parameters)
        vacancy_ids = self.get_vacancy_ids(limit=limit, pages=pages)
        
        for vacancy_id in vacancy_ids:
            response = await self.rps_limiter.request(self.http_client.get, f"{app_settings.VIEW_URL}{vacancy_id}", follow_redirects=True, params=view_query_parameters)
            response.raise_for_status()
            vacancy = response.json()
            vacancies.append(vacancy)
            
        return vacancies