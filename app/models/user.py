from sqlalchemy import Column, Integer, String, Date, Boolean

from app.core.database import Base


class User(Base):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    erstellt_am = Column(Date, nullable=False)
