from abc import ABC, abstractmethod

from app.core.database import async_session_maker


class Repository(ABC):
    
    @abstractmethod
    def get_one():
        pass
    
    
    @abstractmethod
    def get_all():
        pass
    
    
    @abstractmethod
    def create():
        pass
    

class SQLAlchemyRepository(Repository):
    model = None
    
    async def get_one(self):
        
        async with async_session_maker() as session:
            pass
        
        
    async def get_all(self):
        
        async with async_session_maker() as session:
            pass
        
        
    async def create(self):
        
        async with async_session_maker() as session:
            pass
    
