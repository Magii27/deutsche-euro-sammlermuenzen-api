from typing import Type

from sqlalchemy.orm import Session
from app.models import Kuenstler
from typing import Type, Optional


class KuenstlerRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Kuenstler]:
        return self._session.query(Kuenstler).all()

    def get_by_id(self, kuenstler_id: int) -> Optional[Kuenstler]:
        return (self._session
                .query(Kuenstler)
                .filter(Kuenstler.id == kuenstler_id)
                .first())

    def create(self, kuenstler: Kuenstler) -> Kuenstler:
        self._session.add(kuenstler)
        self._session.commit()
        self._session.refresh(kuenstler)

        return kuenstler

    def update(self, kuenstler: Kuenstler) -> Kuenstler:
        existing_kuenstler = self.get_by_id(kuenstler.id)

        if not existing_kuenstler:
            raise ValueError("")

        for key, value in kuenstler.__dict__.items():
            if key != '_sa_instance_state':
                setattr(existing_kuenstler, key, value)

        self._session.commit()
        self._session.refresh(existing_kuenstler)

        return existing_kuenstler

    def delete(self, kuenstler_id: int) -> None:
        existing_kuenstler = self.get_by_id(kuenstler_id)

        if not existing_kuenstler:
            raise ValueError("")

        self._session.delete(existing_kuenstler)
        self._session.commit()
