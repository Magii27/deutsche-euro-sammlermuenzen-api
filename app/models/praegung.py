from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base  # Base kommt aus deinem DB-Setup


class Praegung(Base):
    __tablename__ = "t_praegung"

    id = Column(Integer, primary_key=True, index=True)
    herkunftsbezeichnung = Column(String, nullable=False)
    standort = Column(String, nullable=False)
