from pydantic import BaseModel
from typing import Optional


class MaterialBaseSchema(BaseModel):
    bezeichnung: str
    spezifikation: str


class MaterialCreateSchema(MaterialBaseSchema):
    pass


class MaterialUpdateSchema(MaterialBaseSchema):
    bezeichnung: Optional[str] = None
    spezifikation: Optional[str] = None


class MaterialSchema(MaterialBaseSchema):
    id: int

    class Config:
        from_attributes = True
