from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Polymerring(Base):
    __tablename__ = "t_polymerring"

    id = Column(Integer, primary_key=True, index=True)
    farbe = Column(String, nullable=False)
