from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from httpx import AsyncClient

from app.db import create_tables
from app.router import router
from app.rps_limiter import RPSLimiter


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    app.state.http_client = AsyncClient()
    app.state.rps_limiter = RPSLimiter()
    
    yield
    
    await app.state.http_client.aclose()
  
app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="app.main:app", reload=True)
