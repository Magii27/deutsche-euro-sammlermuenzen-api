from pydantic import BaseModel
from typing import Optional


class SerieMuenzeBaseSchema(BaseModel):
    serie_id: int
    muenze_id: int
    reihenfolge: int


class SerieMuenzeCreateSchema(SerieMuenzeBaseSchema):
    pass


class SerieMuenzeUpdateSchema(SerieMuenzeBaseSchema):
    serie_id: Optional[int] = None
    muenze_id: Optional[int] = None
    reihenfolge: Optional[int] = None


class SerieMuenzeSchema(SerieMuenzeBaseSchema):
    id: int

    class Config:
        from_attributes = True
