from typing import Type, Optional

from app.models import SerieMuenze, Muenze, Serie

from sqlalchemy.orm import Session


class SerieMuenzeRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Type[SerieMuenze]]:
        return self._session.query(SerieMuenze).all()

    def get_muenze_by_serie(self, serie_id: int) -> list[Type[Muenze]]:
        return self._session.query(SerieMuenze).filter(SerieMuenze.serie_id == serie_id).all()

    def get_serie_by_muenze(self, muenze_id: int) -> Serie:
        return self._session.query(SerieMuenze).filter(SerieMuenze.muenze_id == muenze_id).first().first()

    def get_by_id(self, serien_muenze_id: int) -> Optional[SerieMuenze]:
        return (self._session
                .query(SerieMuenze)
                .filter(SerieMuenze.id == serien_muenze_id)
                .first())

    def create(self, serien_muenze: SerieMuenze) -> SerieMuenze:
        self._session.add(serien_muenze)
        self._session.commit()
        self._session.refresh(serien_muenze)

        return serien_muenze

    def update(self, serien_muenze: SerieMuenze) -> SerieMuenze:
        existing_serien_muenze = self.get_by_id(serien_muenze.id)

        if not existing_serien_muenze:
            raise ValueError("")

        for key, value in serien_muenze.__dict__.items():
            if key != '_sa_instance_state':
                setattr(existing_serien_muenze, key, value)

        self._session.commit()
        self._session.refresh(existing_serien_muenze)

        return existing_serien_muenze

    def delete(self, serien_muenze_id: int) -> None:
        existing_serien_muenze = self.get_by_id(serien_muenze_id)

        if not existing_serien_muenze:
            raise ValueError("")

        self._session.delete(existing_serien_muenze)
        self._session.commit()
