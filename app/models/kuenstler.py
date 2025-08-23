from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base  # Base kommt aus deinem DB-Setup


class Kuenstler(Base):
    __tablename__ = "t_kuenstler"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
