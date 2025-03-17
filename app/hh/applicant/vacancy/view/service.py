import requests
from fastapi import HTTPException

from app.core.config import HHSettings
from app.core.repositories import Repository

from .schemas import HeaderParameters

hh = HHSettings()


class Service:
    
    
    def __init__(self, repo: Repository):
        self.repo = repo
        self.header_parameters = HeaderParameters().model_dump()
        
    
    async def view(self, 
                   vacancy_id: str,
                   query_parameters: dict):
        url = f"{hh.VACANCIES_URL}{vacancy_id}"
        response = requests.get(
            url=url,
            params=query_parameters,
            headers=self.header_parameters,
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
        return response.json()
