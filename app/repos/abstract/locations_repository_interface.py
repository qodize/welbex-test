import abc

from app.dto.location import Location


class LocationsRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    async def get_locations(self) -> list[Location]:
        ...