import pytest
from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError
from src.models import User
from src.repositories.errors import EntityNotFound, EntityNotUnique
from src.repositories.user_repo import UserRepository


async def test_user_repo_create_can_successfully_create_user_in_the_db(user_repository: UserRepository, db_session):
    user_instance = User(email="some email", username="some username", password="some password")

    actual_user_instance = await user_repository.create(user_instance)

    assert user_instance == actual_user_instance
    db_session.add.assert_called_once_with(user_instance)
    db_session.commit.assert_awaited_once_with()


async def test_user_repo_create_raise_error_when_user_is_not_unique(user_repository: UserRepository, db_session):
    user_instance = User(email="some email", username="some username", password="some password")
    db_session.add.side_effect = IntegrityError(None, None, orig=Exception())
    db_session.add.side_effect.orig.__cause__ = UniqueViolationError()

    with pytest.raises(EntityNotUnique):
        await user_repository.create(user_instance)

    db_session.rollback.assert_awaited_once_with()
    db_session.add.assert_called_once_with(user_instance)


async def test_user_repo_get_can_successfully_get_user_by_id(user_repository: UserRepository, db_session):
    user_instance = User(id="some valid id")
    db_session.get.return_value = user_instance

    actual_team = await user_repository.get(User, user_instance.id)

    assert actual_team == user_instance
    db_session.get.assert_awaited_once_with(entity=User, ident=user_instance.id)


async def test_user_repo_get_raise_error_when_user_does_not_exist(user_repository: UserRepository, db_session):
    user_instance = User(id="some not existing id")
    db_session.get.return_value = None

    with pytest.raises(EntityNotFound):
        await user_repository.get(User, user_instance.id)

    db_session.get.assert_awaited_once_with(entity=User, ident=user_instance.id)
