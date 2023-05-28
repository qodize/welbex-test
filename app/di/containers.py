import os

from dependency_injector import containers, providers

from app.db.database import Database
from app.repos.impl.locations_repository import LocationsRepository
from app.repos.impl.shipments_repository import ShipmentsRepository
from app.repos.impl.transports_repository import TransportsRepository
from app.services.shipments_service import ShipmentsService
from app.services.transports_service import TransportsService
from app.services.updater_service import UpdaterService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.routers"])

    db = providers.Singleton(
        Database,
        f'postgresql+asyncpg://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_SERVER"]}/{os.environ["POSTGRES_DB"]}'
    )

    locations_repository = providers.Factory(
        LocationsRepository,
        session_factory=db.provided.session
    )

    transports_repository = providers.Factory(
        TransportsRepository,
        session_factory=db.provided.session
    )

    shipments_repository = providers.Factory(
        ShipmentsRepository,
        session_factory=db.provided.session
    )

    transports_service = providers.Factory(
        TransportsService,
        transports_repository.provided
    )

    shipments_service = providers.Factory(
        ShipmentsService,
        shipments_repository.provided
    )

    updater_service = providers.Singleton(
        UpdaterService,
        transports_repository.provided,
        locations_repository.provided
    )
