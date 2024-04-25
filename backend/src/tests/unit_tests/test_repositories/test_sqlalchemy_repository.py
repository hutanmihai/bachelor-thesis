import pytest
from asyncpg.exceptions import ForeignKeyViolationError, UniqueViolationError
from sqlalchemy.exc import IntegrityError
from src.models.base import BaseModel
from src.repositories.errors import EntityNotFound, EntityNotUnique
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository


async def test_sqlalchemy_repo_create_can_successfully_create_entity_in_the_db(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    entity_instance = BaseModel()

    actual_entity_instance = await sqlalchemy_repository.create(entity_instance)

    assert entity_instance == actual_entity_instance
    db_session.add.assert_called_once_with(entity_instance)


async def test_sqlalchemy_repo_create_raise_error_when_entity_is_not_unique(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    entity_instance = BaseModel()
    db_session.add.side_effect = IntegrityError(None, None, orig=Exception())
    db_session.add.side_effect.orig.__cause__ = UniqueViolationError()

    with pytest.raises(EntityNotUnique):
        await sqlalchemy_repository.create(entity_instance)

    db_session.rollback.assert_awaited_once_with()
    db_session.add.assert_called_once_with(entity_instance)


async def test_sqlalchemy_repo_create_raise_error_when_entity_does_not_exist(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    entity_instance = BaseModel()
    db_session.add.side_effect = IntegrityError(None, None, orig=Exception())
    db_session.add.side_effect.orig.__cause__ = ForeignKeyViolationError()

    with pytest.raises(EntityNotFound):
        await sqlalchemy_repository.create(entity_instance)

    db_session.rollback.assert_awaited_once_with()
    db_session.add.assert_called_once_with(entity_instance)


async def test_sqlalchemy_repo_get_successfully_get_entity_by_id(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    entity_instance = BaseModel()
    entity_id = "some_team_id"
    db_session.get.return_value = entity_instance

    actual_entity = await sqlalchemy_repository.get(BaseModel, entity_id)

    assert actual_entity == entity_instance
    db_session.get.assert_awaited_once_with(entity=BaseModel, ident=entity_id)


async def test_sqlalchemy_repo_get_raise_error_when_entity_does_not_exist(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    entity_id = "some_team_id"
    db_session.get.return_value = None

    with pytest.raises(EntityNotFound):
        await sqlalchemy_repository.get(BaseModel, entity_id)

    db_session.get.assert_awaited_once_with(entity=BaseModel, ident=entity_id)


async def test_sqlalchemy_repo_update_successfully_update_entity(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    entity_instance = BaseModel()

    actual_entity = await sqlalchemy_repository.update(entity_instance)

    assert actual_entity == entity_instance
    db_session.add.assert_called_once_with(entity_instance)


async def test_sqlalchemy_repo_update_raise_error_when_entity_is_not_unique(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    entity_instance = BaseModel()
    db_session.add.side_effect = IntegrityError(None, None, orig=Exception())
    db_session.add.side_effect.orig.__cause__ = UniqueViolationError()

    with pytest.raises(EntityNotUnique):
        await sqlalchemy_repository.update(entity_instance)

    db_session.rollback.assert_awaited_once_with()
    db_session.add.assert_called_once_with(entity_instance)


async def test_sqlalchemy_repo_ping_returns_true(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    db_session.scalar.return_value = 1
    assert await sqlalchemy_repository.ping()


async def test_sqlalchemy_repo_ping_returns_false(sqlalchemy_repository: SQLAlchemyRepository, db_session):
    db_session.scalar.return_value = None
    assert not await sqlalchemy_repository.ping()
