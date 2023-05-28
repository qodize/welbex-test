import random

from geopy.distance import geodesic

from app.dto.create_transport import CreateTransport
from app.dto.location import Location
from app.dto.transport import Transport
from app.dto.update_transport import UpdateTransport
from app.repos.abstract.locations_repository_interface import LocationsRepositoryInterface
from app.repos.abstract.transports_repository_interface import TransportsRepositoryInterface


class TransportsService:
    def __init__(
            self,
            transports_repo: TransportsRepositoryInterface,
            locations_repo: LocationsRepositoryInterface
    ):
        self.transports_repo = transports_repo
        self.locations_repo = locations_repo

    async def create_transport(self, create_dto: CreateTransport) -> Transport:
        if create_dto.current_zipcode is None:
            locations = await self.locations_repo.get_locations()
            current_location = random.choice(locations)
            create_dto.current_zipcode = current_location.zipcode
        return await self.transports_repo.create_transport(create_dto)

    async def update_transport(self, transport_id: int, update_dto: UpdateTransport) -> Transport:
        return await self.transports_repo.update_transport(transport_id, update_dto)

    async def get_transports(self) -> list[Transport]:
        return await self.transports_repo.get_transports()

    async def distance(self, from_: Location, to: Location) -> float:
        return geodesic((from_.latitude, from_.longitude), (to.latitude, to.longitude)).m
