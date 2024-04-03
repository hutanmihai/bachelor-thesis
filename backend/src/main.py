from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.apis.auth_api import router as auth_router
from src.apis.health_api import router as health_router
from src.apis.payment_api import router as payment_router
from src.settings import settings
from uvicorn import run as uvicorn_run


def _register_api_handlers(app: FastAPI) -> FastAPI:
    """Register API handlers."""
    app.include_router(health_router)
    app.include_router(auth_router)
    app.include_router(payment_router)
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
    app = FastAPI(version="1.0.0", title="RoCarPrediction API", root_path="/api/v1")
    app = _register_api_handlers(app)
    app = add_middleware(app)
    return app


app: FastAPI = create_app()


def run_app(app: FastAPI = app) -> None:
    """Run FastAPI application."""
    uvicorn_run(app, host=settings.app_host, port=int(settings.app_port))
