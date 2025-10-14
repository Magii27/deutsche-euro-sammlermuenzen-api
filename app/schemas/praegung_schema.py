from pydantic import BaseModel
from typing import Optional


class PraegungBaseSchema(BaseModel):
    herkunftsbezeichnung: str
    standort: str


class PraegungCreateSchema(PraegungBaseSchema):
    pass


class PraegungUpdateSchema(PraegungBaseSchema):
    herkunftsbezeichnung: Optional[str] = None
    standort: Optional[str] = None


class PraegungSchema(PraegungBaseSchema):
    id: int

    class Config:
        from_attributes = True
