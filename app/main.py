from fastapi import FastAPI

from app.di.containers import Container


def create_app() -> FastAPI:
    app = FastAPI()
    container = Container()
    app.container = container

    @app.on_event('startup')
    async def startup():
        await app.container.db().init_models()

    return app


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
