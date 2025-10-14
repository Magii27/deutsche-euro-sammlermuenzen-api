from pydantic import BaseModel
from typing import Optional


class KuenstlerBaseSchema(BaseModel):
    name: str


class KuenstlerCreateSchema(KuenstlerBaseSchema):
    pass


class KuenstlerUpdateSchema(KuenstlerBaseSchema):
    name: Optional[str] = None


class KuenstlerSchema(KuenstlerBaseSchema):
    id: int

    class Config:
        from_attributes = True
