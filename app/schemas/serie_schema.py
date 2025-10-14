from pydantic import BaseModel
from typing import Optional


class SerieBaseSchema(BaseModel):
    bezeichnung: str


class SerieCreateSchema(SerieBaseSchema):
    pass


class SerieUpdateSchema(SerieBaseSchema):
    bezeichnung: Optional[str] = None


class SerieSchema(SerieBaseSchema):
    id: int

    class Config:
        from_attributes = True
