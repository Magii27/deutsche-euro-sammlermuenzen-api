from pydantic import BaseModel
from typing import Optional


class PolymerringBaseSchema(BaseModel):
    farbe: str


class PolymerringCreateSchema(PolymerringBaseSchema):
    pass


class PolymerringUpdateSchema(PolymerringBaseSchema):
    farbe: Optional[str] = None


class PolymerringSchema(PolymerringBaseSchema):
    id: int

    class Config:
        from_attributes = True
