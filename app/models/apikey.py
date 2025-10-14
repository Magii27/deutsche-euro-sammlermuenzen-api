from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.core.database import Base


class ApiKey(Base):
    __tablename__ = "t_apikey"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("t_user.id"), nullable=False)
    api_key = Column(String, nullable=False)
    daily_limit = Column(Integer, nullable=True)
    is_active = Column(Boolean, nullable=False)
