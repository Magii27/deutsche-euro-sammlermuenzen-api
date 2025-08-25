from pydantic import BaseModel
from datetime import date
from typing import Optional


class MuenzeBaseSchema(BaseModel):
    titel: str
    serie_id: int
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
    serie_id: Optional[int] = None
    ausgabedatum: Optional[date] = None
    praegung_id: Optional[int] = None
    kuenstler_id: Optional[int] = None
    material_id: Optional[int] = None
    polymerring_id: Optional[int] = None
    gewicht: Optional[float] = None
    masse: Optional[float] = None


class MuenzeSchema(MuenzeBaseSchema):
    id: int

    class Config:
        orm_mode = True
