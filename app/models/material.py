from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Material(Base):
    __tablename__ = "t_material"

    id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String, nullable=False)
    spezifikation = Column(String, nullable=True)
