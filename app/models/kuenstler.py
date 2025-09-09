from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Kuenstler(Base):
    __tablename__ = "t_kuenstler"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
