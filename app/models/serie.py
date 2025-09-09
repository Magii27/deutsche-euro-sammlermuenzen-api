from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Serie(Base):
    __tablename__ = "t_serie"

    id = Column(Integer, primary_key=True, index=True)
    bezeichnung = Column(String, nullable=False)