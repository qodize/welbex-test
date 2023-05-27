from contextlib import AbstractAsyncContextManager
from typing import Optional, Callable

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.mappers.mappers import mappers
from app.db.models.shipment_model import ShipmentModel
from app.dto.create_shipment import CreateShipment
from app.dto.shipment import Shipment
from app.dto.update_shipment import UpdateShipment
from app.exceptions.not_found_error import NotFoundError
from app.exceptions.zipcode_not_found_error import ZipcodeNotFoundError
from app.repos.abstract.shipments_repository_interface import ShipmentsRepositoryInterface


class ShipmentsRepository(ShipmentsRepositoryInterface):
    def __init__(
            self,
            session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        self.session_factory = session_factory

    async def create_shipment(self, create_dto: CreateShipment) -> Shipment:
        async with self.session_factory() as session:
            try:
                shipment_model = mappers[CreateShipment][ShipmentModel](create_dto)
                session.add(shipment_model)
                await session.commit()
                await session.refresh(shipment_model)
                return mappers[ShipmentModel][Shipment](shipment_model)
            except SQLAlchemyError:
                raise ZipcodeNotFoundError()

    async def get_shipments(self, min_weight: Optional[int] = None, max_weight: Optional[int] = None) -> list[Shipment]:
        async with self.session_factory() as session:
            return [
                mappers[ShipmentModel][Shipment](shipment_model)
                for shipment_model in (await session.execute(select(ShipmentModel))).scalars()
            ]

    async def get_shipment(self, shipment_id: int) -> Shipment:
        async with self.session_factory() as session:
            try:
                return mappers[ShipmentModel][Shipment](
                    (await session.execute(
                        select(ShipmentModel).filter(ShipmentModel.shipment_id == shipment_id)
                    )).scalar_one()
                )
            except SQLAlchemyError:
                raise NotFoundError()

    async def update_shipment(self, shipment_id: int, update_dto: UpdateShipment) -> Shipment:
        async with self.session_factory() as session:
            try:
                shipment_model = (await session.execute(
                    select(ShipmentModel).filter(ShipmentModel.shipment_id == shipment_id)
                )).scalar_one()
            except SQLAlchemyError:
                raise NotFoundError()
            if update_dto.weight is not None:
                shipment_model.weight = update_dto.weight
            if update_dto is not None:
                shipment_model.description = update_dto.description
            session.add(shipment_model)
            await session.commit()
            await session.refresh(shipment_model)
            return mappers[ShipmentModel][Shipment](shipment_model)

    async def delete_shipment(self, shipment_id: int) -> None:
        async with self.session_factory() as session:
            try:
                shipment_model = (await session.execute(
                    select(ShipmentModel).filter(ShipmentModel.shipment_id == shipment_id)
                )).scalar_one()
            except SQLAlchemyError:
                raise NotFoundError()
            await session.delete(shipment_model)
            await session.commit()
