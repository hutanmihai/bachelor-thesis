import asyncio
import os
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from src import models
from src.database import async_engine, async_session
from src.download import S3_DIR_PATH, download_dirs_from_s3
from src.main import app
from src.ml import get_models_and_preprocessors, ml_ops


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def init_models():
    # Download models and preprocessors from S3 if they do not exist
    if not os.path.exists(S3_DIR_PATH):
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


@pytest.fixture(scope="session", autouse=True)
async def db_tables() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(models.BaseModel.metadata.drop_all)
        await conn.run_sync(models.BaseModel.metadata.create_all)


@pytest.fixture
async def session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session(autoflush=False, autocommit=False) as sess:
        yield sess
        await sess.rollback()


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client
