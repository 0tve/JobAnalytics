from app.core.repositories import SQLAlchemyRepository
from app.hh.applicant.vacancy.view.models import Response


class Repository(SQLAlchemyRepository):
    model = Response