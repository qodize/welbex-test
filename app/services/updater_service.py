import asyncio
import random

from app.dto.update_transport import UpdateTransport
from app.repos.abstract.locations_repository_interface import LocationsRepositoryInterface
from app.repos.abstract.transports_repository_interface import TransportsRepositoryInterface


class UpdaterService:
    def __init__(
            self,
            transport_repo: TransportsRepositoryInterface,
            locations_repo: LocationsRepositoryInterface
    ):
        self.transport_repo = transport_repo
        self.locations_repo = locations_repo

    async def start_updating(self):
        while True:
            await asyncio.sleep(3 * 60)
            transports = await self.transport_repo.get_transports()
            locations = await self.locations_repo.get_locations()
            for transport in transports:
                await self.transport_repo.update_transport(
                    transport.transport_id,
                    UpdateTransport(
                        current_zipcode=random.choice(locations).zipcode
                    )
                )
