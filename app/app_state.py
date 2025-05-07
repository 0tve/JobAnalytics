from fastapi import Request
from httpx import AsyncClient
from app.rps_limiter import RPSLimiter


def get_http_client(request: Request) -> AsyncClient:
    return request.app.state.http_client

def get_rps_limiter(request: Request) -> RPSLimiter:
    return request.app.state.rps_limiter