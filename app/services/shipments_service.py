from app.dto.create_shipment import CreateShipment
from app.dto.shipments_list_item import ShipmentsListItem
from app.dto.single_shipment import SingleShipment
from app.dto.update_shipment import UpdateShipment
from app.exceptions.not_found_error import NotFoundError
from app.repos.abstract.shipments_repository_interface import ShipmentsRepositoryInterface


class ShipmentsService:
    def __init__(
            self,
            shipments_repo: ShipmentsRepositoryInterface,
    ):
        self.shipments_repo = shipments_repo

    async def create_shipment(self, create_dto: CreateShipment) -> SingleShipment:
        try:
            return await self.shipments_repo.create_shipment(create_dto)
        except NotFoundError as e:
            raise e

    async def get_shipments(
            self,
            min_weight: int,
            max_weight: int,
            max_transport_distance: int
    ) -> list[ShipmentsListItem]:
        return await self.shipments_repo.get_shipments(min_weight, max_weight, max_transport_distance)

    async def get_shipment(self, shipment_id: int) -> SingleShipment:
        try:
            return await self.shipments_repo.get_shipment(shipment_id)
        except NotFoundError as e:
            raise e

    async def update_shipment(self, shipment_id: int, update_dto: UpdateShipment) -> SingleShipment:
        try:
            return await self.shipments_repo.update_shipment(shipment_id, update_dto)
        except NotFoundError as e:
            raise e

    async def delete_shipment(self, shipment_id: int) -> None:
        try:
            return await self.shipments_repo.delete_shipment(shipment_id)
        except NotFoundError as e:
            raise e
