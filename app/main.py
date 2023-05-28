import asyncio

from fastapi import FastAPI

from app.di.containers import Container
from app.routers import shipments_router, transports_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(shipments_router.router)
    app.include_router(transports_router.router)

    container = Container()
    app.container = container

    @app.on_event('startup')
    async def startup():
        await app.container.db().init_models()
        asyncio.create_task(app.container.updater_service().start_updating())

    return app


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
