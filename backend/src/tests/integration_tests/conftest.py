import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import async_engine, async_session
from src.main import app

from src import models


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


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
