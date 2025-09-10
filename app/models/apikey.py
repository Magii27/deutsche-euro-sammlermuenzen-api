from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float

from app.core.database import Base


class ApiKey(Base):
    __tablename__ = "t_apikey"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("t_user.id"), nullable=False)
    api_key = Column(String, nullable=False)
    daily_limit = Column(Date, nullable=True)
    is_active = Column(Float, nullable=False)
