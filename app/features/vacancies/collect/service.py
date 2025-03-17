from app.hh.applicant.vacancy.view.schemas import \
    QueryParameters as ViewQueryParameters
from app.hh.applicant.vacancy.view.service import Service as ViewService
from app.hh.public.vacancies.search.schemas import \
    QueryParameters as SearchQueryParameters
from app.hh.public.vacancies.search.service import Service as SearchService

from .repository import Repository

# TODO: limit rps
class Service:
    
    
    def __init__(self, repo: Repository, view_service: ViewService, search_service: SearchService):
        self.repo = repo
        self.view_service = view_service
        self.search_service = search_service
    
    
    async def collect_pages(self, limit: int, search_query_parameters: SearchQueryParameters):
        pages = []
        search_result = await self.search_service.search(query_parameters=search_query_parameters)
        per_page = search_result["per_page"]
        found = search_result["found"]
        vacancies_to_collect = found if found < limit else limit
        pages_to_collect = -(-vacancies_to_collect // per_page)
        
        for page in range(pages_to_collect):
            search_query_parameters.page = page
            result = await self.search_service.search(query_parameters=search_query_parameters)
            pages.append(result)
            
        return pages
    
    
    async def get_vacancy_ids(self, limit: int, pages: list[dict]):
        vacancy_ids = []
        
        for page in pages:
            vacancy_ids.extend([vacancy["id"] for vacancy in page["items"]])
            
        return vacancy_ids[:limit]
    
    
    async def collect(self, limit: int, search_query_parameters: SearchQueryParameters):
        vacancies = []
        view_query_parameters = ViewQueryParameters(locale=search_query_parameters.locale, host=search_query_parameters.host).model_dump(exclude_none=True)
        pages = await self.collect_pages(limit=limit, search_query_parameters=search_query_parameters)
        vacancy_ids = await self.get_vacancy_ids(limit=limit, pages=pages)
        
        for vacancy_id in vacancy_ids:
            vacancy = await self.view_service.view(vacancy_id=vacancy_id, 
                                                   query_parameters=view_query_parameters)
            vacancies.append(vacancy)
            
        return vacancies
