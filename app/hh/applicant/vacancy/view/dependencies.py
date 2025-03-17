from .repository import Repository
from .service import Service


def get_service():
    return Service(Repository)
