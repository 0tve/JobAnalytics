from app.core.repositories import SQLAlchemyRepository

from .models import Response


class Repository(SQLAlchemyRepository):
    model = Response