from unittest import mock

import pytest
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository
from src.repositories.user_repo import UserRepository
from src.services.health_srv import HealthSrv
from src.services.user_srv import UserSrv


def pytest_collection_modifyitems(config, items):
    for item in items:
        if "asyncio" in item.keywords:
            item.add_marker(pytest.mark.asyncio)


@pytest.fixture
async def db_session():
    add_mock = mock.Mock(name="db_session.add mock")
    scalar_mock = mock.AsyncMock(name="db_session.execute mock")
    scalars_mock = mock.AsyncMock(name="db_session.scalars mock")
    get_mock = mock.AsyncMock(name="db_session.get mock")
    return mock.AsyncMock(
        add=add_mock,
        scalar=scalar_mock,
        scalars=scalars_mock,
        get=get_mock,
        name="async session mock",
    )


@pytest.fixture
async def user_repository_mock():
    create_mock = mock.AsyncMock(name="user_repository.create mock")
    get_mock = mock.AsyncMock(name="user_repository.get mock")
    return mock.AsyncMock(
        create=create_mock,
        get=get_mock,
        name="async user_repository mock",
    )


@pytest.fixture
async def sqlalchemy_repository_mock():
    create_mock = mock.AsyncMock(name="sqlalchemy_repository.create mock")
    ping_mock = mock.AsyncMock(name="sqlalchemy_repository.ping mock")
    return mock.AsyncMock(
        create=create_mock,
        ping=ping_mock,
        name="async sqlalchemy_repository mock",
    )


@pytest.fixture
async def sqlalchemy_repository(db_session) -> SQLAlchemyRepository:
    return SQLAlchemyRepository(db_session)


@pytest.fixture
async def user_repository(db_session) -> UserRepository:
    return UserRepository(db_session)


@pytest.fixture
async def user_service(user_repository_mock) -> UserSrv:
    return UserSrv(repo=user_repository_mock)


@pytest.fixture
async def health_service(sqlalchemy_repository_mock) -> HealthSrv:
    return HealthSrv(repo=sqlalchemy_repository_mock)
