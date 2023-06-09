import abc
from typing import Optional

from app.dto.create_shipment import CreateShipment
from app.dto.shipment import Shipment
from app.dto.update_shipment import UpdateShipment


class ShipmentsRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    async def create_shipment(self, create_dto: CreateShipment) -> Shipment:
        ...

    @abc.abstractmethod
    async def get_shipments(
            self,
            min_weight: Optional[int] = None,
            max_weight: Optional[int] = None,
    ) -> list[Shipment]:
        ...

    @abc.abstractmethod
    async def get_shipment(self, shipment_id: int) -> Shipment:
        ...

    @abc.abstractmethod
    async def update_shipment(self, shipment_id: int, update_dto: UpdateShipment) -> Shipment:
        ...

    @abc.abstractmethod
    async def delete_shipment(self, shipment_id: int) -> None:
        ...
