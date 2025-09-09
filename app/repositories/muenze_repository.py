from typing import Type, Optional
from sqlalchemy.orm import Session
from sqlalchemy import extract
from app.models import Muenze, SerieMuenze


class MuenzeRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Type[Muenze]]:
        return self._session.query(Muenze).all()

    def get_filtered(self,
                     serie_id: Optional[int] = None,
                     praegung_id: Optional[int] = None,
                     ausgabejahr: Optional[int] = None,
                     kuenstler_id: Optional[int] = None,
                     material_id: Optional[int] = None,
                     polymerring: Optional[bool] = None,
                     polymerring_id: Optional[int] = None
                     ) -> list[Type[Muenze]]:
        query = self._session.query(Muenze)

        if serie_id:
            query = query.filter(Muenze.serie_id == serie_id)

        if praegung_id:
            query = query.filter(Muenze.praegung_id == praegung_id)

        if ausgabejahr:
            query = query.filter(extract("year", Muenze.ausgabedatum) == ausgabejahr)

        if kuenstler_id:
            query = query.filter(Muenze.kuenstler_id == kuenstler_id)

        if material_id:
            query = query.filter(Muenze.material_id == material_id)

        if polymerring:
            query = query.filter(Muenze.polymerring_id.isnot(None))

        if polymerring_id:
            query = query.filter(Muenze.polymerring_id == polymerring_id)

    def get_by_id(self, muenze_id: int) -> Optional[Muenze]:
        return (self._session
                .query(Muenze)
                .filter(Muenze.id == muenze_id)
                .first())

    def get_reihenfolge_by_id(self, muenze_id: int) -> Optional[SerieMuenze]:
        return (self._session
                .query(SerieMuenze)
                .filter(SerieMuenze.muenze_id == muenze_id)
                .first())

    def create(self, muenze: Muenze) -> Muenze:
        self._session.add(muenze)
        self._session.commit()
        self._session.refresh(muenze)

        return muenze

    def update(self, muenze: Muenze) -> Muenze:
        existing_muenze = self.get_by_id(muenze.id)

        if not existing_muenze:
            raise ValueError(f"Muenze with id {muenze.id} does not exist.")

        for key, value in muenze.__dict__.items():
            if key != '_sa_instance_state':
                setattr(existing_muenze, key, value)

        self._session.commit()
        self._session.refresh(existing_muenze)

        return existing_muenze

    def delete(self, muenze_id: int) -> None:
        existing_muenze = self.get_by_id(muenze_id)

        if not existing_muenze:
            raise ValueError(f"ding")

        self._session.delete(existing_muenze)
        self._session.commit()
