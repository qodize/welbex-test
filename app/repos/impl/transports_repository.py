from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.mappers.mappers import mappers
from app.db.models.transport_model import TransportModel
from app.dto.create_transport import CreateTransport
from app.dto.transport import Transport
from app.dto.update_transport import UpdateTransport
from app.exceptions.not_found_error import NotFoundError
from app.exceptions.zipcode_not_found_error import ZipcodeNotFoundError
from app.repos.abstract.transports_repository_interface import TransportsRepositoryInterface


class TransportsRepository(TransportsRepositoryInterface):
    def __init__(
            self,
            session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        self.session_factory = session_factory

    async def create_transport(self, create_dto: CreateTransport) -> Transport:
        async with self.session_factory() as session:
            try:
                transport_model = mappers[CreateTransport][TransportModel](create_dto)
                session.add(transport_model)
                await session.commit()
                await session.refresh(transport_model)
                return mappers[TransportModel][Transport](transport_model)
            except SQLAlchemyError:
                raise ZipcodeNotFoundError()

    async def update_transport(self, transport_id: int, update_dto: UpdateTransport) -> Transport:
        async with self.session_factory() as session:
            try:
                transport_model: TransportModel = (await session.execute(
                    select(TransportModel).filter(TransportModel.transport_id == transport_id)
                )).scalar_one()
            except SQLAlchemyError:
                raise NotFoundError()
            try:
                if update_dto.current_zipcode:
                    transport_model.current_zipcode = update_dto.current_zipcode
                session.add(transport_model)
                await session.commit()
            except SQLAlchemyError:
                raise ZipcodeNotFoundError()
            await session.refresh(transport_model)
            return mappers[TransportModel][Transport](transport_model)

    async def get_transports(self) -> list[Transport]:
        async with self.session_factory() as session:
            return [
                mappers[TransportModel][Transport](transport_model)
                for transport_model in (await session.execute(select(TransportModel))).scalars()
            ]
