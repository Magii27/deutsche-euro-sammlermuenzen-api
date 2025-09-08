from pydantic import BaseModel
from typing import Optional


class PraegungBaseSchema(BaseModel):
    herkunftsbezeichnung: str
    standort: str


class PraegungCreateSchema(PraegungBaseSchema):
    pass


class PraegungUpdateSchema(PraegungBaseSchema):
    titel: Optional[str] = None
    standort: Optional[str] = None


class PraegungeSchema(PraegungBaseSchema):
    id: int

    class Config:
        orm_mode = True
