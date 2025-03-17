from app.hh.applicant.vacancy.view.service import Service as ViewService
from app.hh.public.vacancies.search.service import Service as SearchService

from .repository import Repository
from .service import Service


def get_service():
    return Service(Repository, ViewService(Repository), SearchService(Repository))