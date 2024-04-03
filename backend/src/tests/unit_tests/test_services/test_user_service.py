import pytest
from src.models import User
from src.repositories.errors import EntityNotFound, EntityNotUnique
from src.services.errors import UserAlreadyExists, UserNotFound
from src.services.user_srv import UserSrv


async def test_user_service_create_can_successfully_create_user(user_service: UserSrv, user_repository_mock):
    user_instance = User(email="some email", username="some username", password="some password")
    user_repository_mock.create.return_value = user_instance

    actual_user_instance = await user_service.new_user(email=user_instance.email, username=user_instance.username, password=user_instance.password)

    assert actual_user_instance == user_instance
    user_repository_mock.create.assert_awaited_once()


async def test_user_service_create_raise_error_when_user_is_not_unique(user_service: UserSrv, user_repository_mock):
    user_instance = User(email="some email", username="some username", password="some password")
    user_repository_mock.create.side_effect = EntityNotUnique(user_instance)

    with pytest.raises(UserAlreadyExists):
        await user_service.new_user(email=user_instance.email, username=user_instance.username, password=user_instance.password)

    user_repository_mock.create.assert_awaited_once()


async def test_user_get_can_successfully_get_user_by_id(user_service: UserSrv, user_repository_mock):
    user_instance = User(id="some valid id", email="some email", username="some username", password="some password")
    user_repository_mock.get.return_value = user_instance

    actual_user_instance = await user_service.get_user(user_id=user_instance.id)

    assert actual_user_instance == user_instance
    user_repository_mock.get.assert_awaited_once_with(User, user_instance.id)


async def test_user_get_raise_error_when_user_is_not_found(user_service: UserSrv, user_repository_mock):
    user_instance = User(
        id="some not existing id",
        email="some email",
        username="some username",
        password="some password",
    )
    user_repository_mock.get.side_effect = EntityNotFound()

    with pytest.raises(UserNotFound):
        await user_service.get_user(user_id=user_instance.id)

    user_repository_mock.get.assert_awaited_once_with(User, user_instance.id)
