from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from httpx import AsyncClient

from app.core.config import AppSettings
from app.core.database import create_schemas, create_tables
from app.features.router import router as features_router
from app.hh.router import router as hh_router

app_settings = AppSettings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_schemas()
    await create_tables()
    app.state.http_client = AsyncClient(base_url=app_settings.BASE_URL)
    
    yield
    
    await app.state.http_client.aclose()
  
app = FastAPI(lifespan=lifespan)
app.include_router(hh_router)
app.include_router(features_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)