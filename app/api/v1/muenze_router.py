from fastapi import APIRouter, Depends
from typing import List, Optional
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.muenze_schema import MuenzeSchema
from app.repositories.muenze_repository import MuenzeRepository

muenze_router = APIRouter(prefix="/muenzen", tags=["muenzen"])


@muenze_router.get("/", response_model=List[MuenzeSchema])
async def get_muenzen(
        serie_id: Optional[int] = None,
        praegung_id: Optional[int] = None,
        kuenstler_id: Optional[int] = None,
        material_id: Optional[int] = None,
        polymerring: Optional[bool] = None,
        polymerring_id: Optional[int] = None,
        db: Session = Depends(get_db)
):
    """Alle Münzen + Filtermöglichkeiten"""

    repo = MuenzeRepository(db)

    if polymerring is False and polymerring_id:
        polymerring = None

    return repo.get_filtered(
        serie_id=serie_id,
        praegung_id=praegung_id,
        kuenstler_id=kuenstler_id,
        material_id=material_id,
        polymerring=polymerring,
        polymerring_id=polymerring_id
    )


@muenze_router.get("/{muenze_id}", response_model=MuenzeSchema)
async def get_muenze_by_id(
        muenze_id: int,
        db: Session = Depends(get_db)
):
    """Informationen zu einer Münze"""
    repo = MuenzeRepository(db)

    return repo.get_by_id(muenze_id)
