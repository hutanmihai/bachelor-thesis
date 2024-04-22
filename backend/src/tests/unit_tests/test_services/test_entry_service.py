import pytest
from src.models import Entry
from src.repositories.errors import EntityNotFound
from src.services.entry_srv import EntrySrv
from src.services.errors import EntryNotCreatedByUser, EntryNotFound


async def test_entry_service_create_can_successfully_create_entry(entry_service: EntrySrv, entry_repository_mock):
    entry_instance = Entry()
    entry_repository_mock.create.return_value = entry_instance
    await entry_service.create_entry(entry_instance)

    entry_repository_mock.create.assert_awaited_once()


async def test_entry_service_get_all_can_successfully_get_all_entries(entry_service: EntrySrv, entry_repository_mock):
    user_id = "some user id"
    entry_instance = Entry(user_id=user_id)
    entry_repository_mock.get_all_entries.return_value = [entry_instance]

    actual_entry_instance = await entry_service.get_all_entries(user_id)

    assert actual_entry_instance == [entry_instance]
    entry_repository_mock.get_all_entries.assert_awaited_once_with(user_id)


async def test_entry_service_can_delete_entry(entry_service: EntrySrv, entry_repository_mock):
    entry_id = "some entry id"
    user_id = "some user id"
    entry_instance = Entry(id=entry_id, user_id=user_id)
    entry_repository_mock.get.return_value = entry_instance

    await entry_service.delete_entry(entry_id, user_id)

    entry_repository_mock.get.assert_awaited_once_with(Entry, entry_id)
    entry_repository_mock.delete.assert_awaited_once_with(entry_instance)


async def test_entry_service_delete_raises_error_when_entry_not_found(entry_service: EntrySrv, entry_repository_mock):
    entry_id = "some not existing entry id"
    user_id = "some user id"
    entry_repository_mock.get.side_effect = EntityNotFound()

    with pytest.raises(EntryNotFound):
        await entry_service.delete_entry(entry_id, user_id)

    entry_repository_mock.get.assert_awaited_once_with(Entry, entry_id)


async def test_entry_service_delete_raises_error_when_user_tries_to_delete_not_owned_entry(entry_service: EntrySrv, entry_repository_mock):
    entry_id = "some entry id"
    user_id = "some user id"
    entry_instance = Entry(id=entry_id, user_id="some other user id")
    entry_repository_mock.get.return_value = entry_instance

    with pytest.raises(EntryNotCreatedByUser):
        await entry_service.delete_entry(entry_id, user_id)

    entry_repository_mock.get.assert_awaited_once_with(Entry, entry_id)
