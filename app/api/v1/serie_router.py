from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.serie_schema import SerieSchema
from app.repositories.serie_repository import SerieRepository

serie_router = APIRouter(prefix="/serien", tags=["serien"])


@serie_router.get("/", response_model=List[SerieSchema])
async def get_serien(
        db: Session = Depends(get_db)
):
    """Alle Serien"""

    repo = SerieRepository(db)

    return repo.get_all()


@serie_router.get("/{serie_id}", response_model=SerieSchema)
async def get_serie_by_id(
        serie_id: int,
        db: Session = Depends(get_db)
):
    """Informationen zu einer Münze"""
    repo = SerieRepository(db)

    return repo.get_by_id(serie_id)
