from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.apis.auth_api import router as auth_router
from src.apis.entry_api import router as entry_router
from src.apis.health_api import router as health_router
from src.apis.inference_api import router as inference_router
from src.apis.payment_api import router as payment_router
from src.apis.user_api import router as user_router
from src.download import download_dirs_from_s3
from src.ml import get_models_and_preprocessors, ml_ops
from src.settings import settings
from uvicorn import run as uvicorn_run


def _register_api_handlers(app: FastAPI) -> FastAPI:
    """Register API handlers."""
    app.include_router(health_router)
    app.include_router(auth_router)
    app.include_router(payment_router)
    app.include_router(inference_router)
    app.include_router(user_router)
    app.include_router(entry_router)
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    download_dirs_from_s3()
    (
        ml_ops.fastvit_model,
        ml_ops.transforms,
        ml_ops.tokenizer,
        ml_ops.bert_model,
        ml_ops.model,
        ml_ops.target_encoder,
        ml_ops.scaler_numerical,
        ml_ops.scaler_categorical,
    ) = get_models_and_preprocessors()
    yield


def create_app() -> FastAPI:
    """Create and return FastAPI application."""
    app = FastAPI(version="1.0.0", title="RoCarPrediction API", root_path="/api/v1", lifespan=lifespan)
    app = _register_api_handlers(app)
    app = add_middleware(app)
    return app


app: FastAPI = create_app()


def run_app(app: FastAPI = app) -> None:
    """Run FastAPI application."""
    uvicorn_run(app, host=settings.app_host, port=int(settings.app_port))
