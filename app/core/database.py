from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import DatabaseSettings
from app.core.models.base import Base

database_settings = DatabaseSettings()
async_engine = create_async_engine(database_settings.DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine)


async def get_async_session(): 
    
    async with async_session_maker() as session:
        yield session


async def create_schemas():
    
    async with async_engine.begin() as conn:
        
        for schema in database_settings.SCHEMAS:
            await conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))


async def create_tables():
    
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)