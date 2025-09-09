from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float

from app.core.database import Base


class Muenze(Base):
    __tablename__ = "t_muenze"

    id = Column(Integer, primary_key=True, index=True)
    titel = Column(String, nullable=False)
    serie_id = Column(Integer, ForeignKey("t_serie.id"), nullable=False)
    ausgabedatum = Column(Date, nullable=False)
    nennwert = Column(Float, nullable=True)
    praegung_id = Column(Integer, ForeignKey("t_praegung.id"), nullable=False)
    kuenstler_id = Column(Integer, ForeignKey("t_kuenstler.id"), nullable=False)
    material_id = Column(Integer, ForeignKey("t_material.id"), nullable=False)
    polymerring_id = Column(Integer, ForeignKey("t_polymerring.id"), nullable=True)
    gewicht = Column(Float, nullable=False)
    masse = Column(Float, nullable=False)
