import abc

from app.dto.create_location import CreateLocation
from app.dto.location import Location


class LocationsRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    async def get_locations(self) -> list[Location]:
        ...

    @abc.abstractmethod
    async def create_location(self, create_dto: CreateLocation) -> Location:
        ...

    @abc.abstractmethod
    async def bulk_create_locations(self, create_dtos: list[CreateLocation]) -> None:
        ...
