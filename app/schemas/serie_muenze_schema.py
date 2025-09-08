from pydantic import BaseModel
from typing import Optional


class SerieMuenzeBaseSchema(BaseModel):
    serie_id: int
    muenze_id: int
    reihenfolge: str


class SerieMuenzeCreateSchema(SerieMuenzeBaseSchema):
    pass


class SerieMuenzeUpdateSchema(SerieMuenzeBaseSchema):
    serie_id: Optional[int] = None
    muenze_id: Optional[int] = None
    reihenfolge: Optional[str] = None


class SerieMuenzeSchema(SerieMuenzeBaseSchema):
    id: int

    class Config:
        orm_mode = True
