from contextlib import AbstractAsyncContextManager
from typing import Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.mappers.mappers import mappers
from app.db.models.location_model import LocationModel
from app.dto.create_location import CreateLocation
from app.dto.location import Location
from app.repos.abstract.locations_repository_interface import LocationsRepositoryInterface


class LocationsRepository(LocationsRepositoryInterface):
    def __init__(
            self,
            session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        self.session_factory = session_factory

    async def get_locations(self) -> list[Location]:
        async with self.session_factory() as session:
            return [
                mappers[LocationModel][Location](location_model)
                for location_model in await session.execute(select(LocationModel))
            ]

    async def create_location(self, create_dto: CreateLocation) -> Location:
        async with self.session_factory() as session:
            location_model = mappers[CreateLocation][LocationModel](create_dto)
            session.add(location_model)
            await session.commit()
            await session.refresh(location_model)
            return mappers[LocationModel][Location](location_model)
