from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base  # Base kommt aus deinem DB-Setup


class Material(Base):
    __tablename__ = "t_material"

    id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String, nullable=False)
    spezifikation = Column(String, nullable=True)
