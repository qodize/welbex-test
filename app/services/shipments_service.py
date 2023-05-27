from typing import Optional

from app.dto.create_shipment import CreateShipment
from app.dto.shipment import Shipment
from app.dto.update_shipment import UpdateShipment
from app.repos.abstract.shipments_repository_interface import ShipmentsRepositoryInterface


class ShipmentsService:
    def __init__(
            self,
            shipments_repo: ShipmentsRepositoryInterface,
    ):
        self.shipments_repo = shipments_repo

    async def create_shipment(self, create_dto: CreateShipment) -> Shipment:
        return await self.shipments_repo.create_shipment(create_dto)

    async def get_shipments(
            self,
            min_weight: Optional[int] = None,
            max_weight: Optional[int] = None,
    ) -> list[Shipment]:
        return await self.shipments_repo.get_shipments(min_weight, max_weight)

    async def get_shipment(self, shipment_id: int) -> Shipment:
        return await self.shipments_repo.get_shipment(shipment_id)

    async def update_shipment(self, shipment_id: int, update_dto: UpdateShipment) -> Shipment:
        return await self.shipments_repo.update_shipment(shipment_id, update_dto)

    async def delete_shipment(self, shipment_id: int) -> None:
        return await self.shipments_repo.delete_shipment(shipment_id)
