import os

from dependency_injector import containers, providers

from app.db.database import Database


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.routers"])

    db = providers.Singleton(
        Database,
        f'postgresql+asyncpg://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_SERVER"]}/{os.environ["POSTGRES_DB"]}'
    )
