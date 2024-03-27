from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.apis.health_api import router as health_router
from src.settings import settings
from uvicorn import run as uvicorn_run


def _register_api_handlers(app: FastAPI) -> FastAPI:
    """Register API handlers."""
    app.include_router(health_router)
    return app


def add_middleware(app: FastAPI) -> FastAPI:
    """Add middleware to FastAPI application."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def create_app() -> FastAPI:
    """Create and return FastAPI application."""
    app = FastAPI()
    app = _register_api_handlers(app)
    app = add_middleware(app)
    return app


app: FastAPI = create_app()


async def run_app(app: FastAPI = app) -> None:
    """Run FastAPI application."""
    uvicorn_run(app, host=settings.app_host, port=int(settings.app_port))
