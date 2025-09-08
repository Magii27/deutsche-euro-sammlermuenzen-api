from typing import Type, Optional

from sqlalchemy.orm import Session

from app.models import Praegung


class PraegungRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Type[Praegung]]:
        return self._session.query(Praegung).all()

    def get_by_id(self, praegung_id: int) -> Optional[Praegung]:
        return (self._session
                .query(Praegung)
                .filter(Praegung.id == praegung_id)
                .first())

    def create(self, praegung: Praegung) -> Praegung:
        self._session.add(Praegung)
        self._session.commit()
        self._session.refresh(praegung)

        return praegung

    def update(self, praegung: Praegung) -> Praegung:
        existing_praegung = self.get_by_id(praegung.id)

        if not existing_praegung:
            raise ValueError("")

        for key, value in praegung.__dict__.items():
            if key != '_sa_instance_state':
                setattr(existing_praegung, key, value)

        self._session.commit()
        self._session.refresh(existing_praegung)

        return existing_praegung

    def delete(self, praegung_id: int) -> None:
        existing_praegung = self.get_by_id(praegung_id)

        if not existing_praegung:
            raise ValueError("")

        self._session.delete(existing_praegung)
        self._session.commit()
