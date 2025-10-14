from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.praegung_schema import PraegungSchema
from app.repositories.praegung_repository import PraegungRepository

praegung_router = APIRouter(prefix="/praegungen", tags=["praegungen"])


@praegung_router.get("/", response_model=List[PraegungSchema])
async def get_praegung(
        db: Session = Depends(get_db)
):
    """Alle Prägungen"""

    repo = PraegungRepository(db)

    return repo.get_all()


@praegung_router.get("/{praegung_id}", response_model=PraegungSchema)
async def get_praegung_by_id(
        praegung_id: int,
        db: Session = Depends(get_db)
):
    """Informationen zu einer Münze"""
    repo = PraegungRepository(db)

    return repo.get_by_id(praegung_id)
