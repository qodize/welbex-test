import abc

from app.dto.create_shipment import CreateShipment
from app.dto.shipments_list_item import ShipmentsListItem
from app.dto.single_shipment import SingleShipment
from app.dto.update_shipment import UpdateShipment


class ShipmentsRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    async def create_shipment(self, create_dto: CreateShipment) -> SingleShipment:
        ...

    @abc.abstractmethod
    async def get_shipments(
            self,
            min_weight: int,
            max_weight: int,
            max_transport_distance: int
    ) -> list[ShipmentsListItem]:
        ...

    @abc.abstractmethod
    async def get_shipment(self, shipment_id: int) -> SingleShipment:
        ...

    @abc.abstractmethod
    async def update_shipment(self, shipment_id: int, update_dto: UpdateShipment) -> SingleShipment:
        ...

    @abc.abstractmethod
    async def delete_shipment(self, shipment_id: int) -> None:
        ...
