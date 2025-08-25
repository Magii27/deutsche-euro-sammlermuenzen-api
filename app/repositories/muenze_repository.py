from typing import Type
from sqlalchemy.orm import Session

from app.models import Muenze


class MuenzeRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Type[Muenze]]:
        return self._session.query(Muenze).all()

    def get_by_id(self, muenze_id: int) -> Muenze | None:
        return (self._session
                .query(Muenze)
                .filter(Muenze.id == muenze_id)
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

        self._session.commit()
        self._session.delete(existing_muenze)
