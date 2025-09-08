from typing import Type, Optional

from app.models import Material
from sqlalchemy.orm import Session


class MaterialRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_all(self) -> list[Type[Material]]:
        return self._session.query(Material).all()

    def get_by_id(self, material_id: int) -> Optional[Material]:
        return (self._session
                .query(Material)
                .filter(Material.id == material_id)
                .first())

    def create(self, material: Material) -> Material:
        self._session.add(material)
        self._session.commit()
        self._session.refresh(material)

        return material

    def update(self, material: Material) -> Material:
        existing_material = self.get_by_id(material.id)

        if not existing_material:
            raise ValueError("")

        for key, value in material.__dict__.items():
            if key != '_sa_instance_state':
                setattr(existing_material, key, value)

        self._session.commit()
        self._session.refresh(existing_material)

        return existing_material

    def delete(self, material_id: int) -> None:
        existing_material = self.get_by_id(material_id)

        if not existing_material:
            raise ValueError("")

        self._session.delete(existing_material)
        self._session.commit()
