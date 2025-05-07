from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import DatabaseSettings
from app.models import Base

database_settings = DatabaseSettings()
async_engine = create_async_engine(database_settings.DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine)

async def create_tables():
    
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)