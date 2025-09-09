from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base  # Base kommt aus deinem DB-Setup


class SerieMuenze(Base):
    __tablename__ = "t_serie_muenze"

    id = Column(Integer, primary_key=True, index=True)
    serie_id = Column(Integer, ForeignKey("t_serie.id"), index=True)
    muenze_id = Column(Integer, ForeignKey("t_muenze.id"), index=True)
    reihenfolge = Column(Integer, nullable=False)

    serie = relationship("Serie", back_populates="muenzen")
    muenze = relationship("Muenze", back_populates="serien")

    __table_args__ = (
        UniqueConstraint("serie_id", "muenze_id", name="uq_serie_muenze"),
        UniqueConstraint("serie_id", "reihenfolge", name="uq_serie_muenze_reihenfolge")
    )
