from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Praegung(Base):
    __tablename__ = "t_praegung"

    id = Column(Integer, primary_key=True, index=True)
    herkunftsbezeichnung = Column(String, nullable=False)
    standort = Column(String, nullable=False)
