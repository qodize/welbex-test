import asyncio
import csv

from fastapi import FastAPI

from app.di.containers import Container
from app.dto.create_location import CreateLocation
from app.exceptions.already_exists_error import AlreadyExistsError
from app.routers import shipments_router, transports_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(shipments_router.router, prefix='/shipments')
    app.include_router(transports_router.router, prefix='/transports')

    container = Container()
    app.container = container

    @app.on_event('startup')
    async def startup():
        await app.container.db().init_models()
        asyncio.create_task(app.container.updater_service().start_updating())
        locations_repo = app.container.locations_repository()
        with open('app/uszips.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            try:
                await locations_repo.bulk_create_locations([
                    CreateLocation(
                        state=row["state_name"],
                        zipcode=row["zip"],
                        latitude=float(row["lat"]),
                        longitude=float(row["lng"])
                    )
                    for row in reader
                ])
            except AlreadyExistsError:
                pass
    return app


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
