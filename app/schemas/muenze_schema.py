from pydantic import BaseModel
from datetime import date
from typing import Optional


class MuenzeBaseSchema(BaseModel):
    titel: str
    ausgabedatum: date
    praegung_id: int
    kuenstler_id: int
    material_id: int
    polymerring_id: int
    gewicht: float
    masse: float


class MuenzeCreateSchema(MuenzeBaseSchema):
    pass


class MuenzeUpdateSchema(MuenzeBaseSchema):
    titel: Optional[str] = None
    ausgabedatum: Optional[date] = None
    nennwert: Optional[float] = None
    praegung_id: Optional[int] = None
    kuenstler_id: Optional[int] = None
    material_id: Optional[int] = None
    polymerring_id: Optional[int] = None
    gewicht: Optional[float] = None
    masse: Optional[float] = None


class MuenzeSchema(MuenzeBaseSchema):
    id: int

    class Config:
        from_attributes = True
