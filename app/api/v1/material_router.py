from fastapi import APIRouter, Depends
from typing import List, Optional
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.material_schema import MaterialSchema
from app.repositories.material_repository import MaterialRepository

material_router = APIRouter(prefix="/materialien", tags=["materialien"])


@material_router.get("/", response_model=List[MaterialSchema])
async def get_materialien(
        db: Session = Depends(get_db)
):
    """Alle Materialien"""

    repo = MaterialRepository(db)

    return repo.get_all()


@material_router.get("/{material_id}", response_model=MaterialSchema)
async def get_material_by_id(
        material_id: int,
        db: Session = Depends(get_db)
):
    """Informationen zu einer Münze"""
    repo = MaterialRepository(db)

    return repo.get_by_id(material_id)
