from fastapi import Depends
from httpx import AsyncClient

from app.core.http_client import get_http_client

from .repository import Repository
from .service import Service


def get_service(http_client: AsyncClient = Depends(get_http_client)):
    return Service(Repository, http_client)