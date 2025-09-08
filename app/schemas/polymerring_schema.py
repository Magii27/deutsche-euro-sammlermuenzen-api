from pydantic import BaseModel
from typing import Optional


class PolymerringBaseSchema(BaseModel):
    farbe: str


class PolymerrinCreateSchema(PolymerringBaseSchema):
    pass


class PolymerrinUpdateSchema(PolymerringBaseSchema):
    farbe: Optional[str] = None


class PolymerrinSchema(PolymerringBaseSchema):
    id: int

    class Config:
        orm_mode = True
