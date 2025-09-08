from typing import Type, Optional

from app.models import Polymerring
from sqlalchemy.orm import Session


class PolymerringRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Type[Polymerring]]:
        return self._session.query(Polymerring).all()

    def get_by_id(self, polymerring_id: int) -> Optional[Polymerring]:
        return (self._session
                .query(Polymerring)
                .filter(Polymerring.id == polymerring_id)
                .first())

    def create(self, polymerring: Polymerring) -> Polymerring:
        self._session.add(polymerring)
        self._session.commit()
        self._session.refresh(polymerring)

        return polymerring

    def update(self, polymerring: Polymerring) -> Polymerring:
        existing_polymerring = self.get_by_id(polymerring.id)

        if not existing_polymerring:
            raise ValueError("")

        for key, value in polymerring.__dict__.items():
            if key != '_sa_instance_none':
                setattr(existing_polymerring, key, value)

        self._session.commit()
        self._session.refresh(existing_polymerring)

        return existing_polymerring

    def delete(self, polymerring_id: Polymerring) -> None:
        existing_polymerring = self.get_by_id(polymerring_id)

        if not existing_polymerring:
            raise ValueError("")

        self._session.delete(existing_polymerring)
        self._session.commit()
