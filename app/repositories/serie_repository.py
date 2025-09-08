from typing import Type, Optional
from app.core.database import Session
from app.models import Serie


class SerieRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Type[Serie]]:
        return self._session.query(Serie).all()

    def get_by_id(self, serie_id: int) -> Optional[Serie]:
        return (self._session
                .query(Serie)
                .filter(Serie.id == serie_id)
                .first())

    def create(self, serie: Serie) -> Serie:
        self._session.add(serie)
        self._session.commit()
        self._session.refresh(serie)

        return serie

    def update(self, serie: Serie) -> Serie:
        existing_serie = self.get_by_id(serie.id)

        if not existing_serie:
            raise ValueError("")

        for key, value in serie.__dict__.items():
            if key != '_sa_instance_state':
                setattr(existing_serie, key, value)

        self._session.commit()
        self._session.refresh(existing_serie)

        return existing_serie

    def delete(self, serie_id: int) -> None:
        existing_serie = self.get_by_id(serie_id)

        if not existing_serie:
            raise ValueError("")

        self._session.delete(existing_serie)
        self._session.commit()
