from app.hh.applicant.vacancy.view.schemas import QueryParameters
from app.hh.applicant.vacancy.view.service import Service as ViewService
from app.hh.public.vacancies.search.service import Service as SearchService

from .repository import Repository

# TODO: pagination
class Service:
    
    
    def __init__(self, repo: Repository, view_service: ViewService, search_service: SearchService):
        self.repo = repo
        self.view_service = view_service
        self.search_service = search_service
    
    
    async def collect(self, search_result: dict, limit: int):
        vacancies = []
        query_parameters = QueryParameters().model_dump(exclude_none=True)
        vacancy_ids = [vacancy["id"] for vacancy in search_result["items"]]
        
        for vacancy_id in vacancy_ids[:limit]:
            vacancy = await self.view_service.view(vacancy_id=vacancy_id,
                                            query_parameters=query_parameters)
            vacancies.append(vacancy)
        
        return vacancies
