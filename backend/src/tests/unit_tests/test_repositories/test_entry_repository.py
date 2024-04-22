import pytest
from sqlalchemy.sql.expression import select
from src.models import Entry, User
from src.repositories.entry_repo import EntryRepository
from src.repositories.errors import EntityNotFound
from src.repositories.user_repo import UserRepository


async def test_entry_repo_create_can_successfully_create_entry_in_the_db(entry_repository: EntryRepository, db_session):
    entry_instance = Entry()

    actual_entry_instance = await entry_repository.create(entry_instance)

    assert entry_instance == actual_entry_instance
    db_session.add.assert_called_once_with(entry_instance)
    db_session.commit.assert_awaited_once_with()


async def test_entry_repo_delete_can_succesfully_delete_entry_in_the_db(entry_repository: EntryRepository, db_session):
    entry_instance = Entry()

    await entry_repository.delete(entry_instance)

    db_session.delete.assert_called_once_with(entry_instance)
    db_session.commit.assert_awaited_once_with()


async def test_user_repo_get_raise_error_when_user_does_not_exist(user_repository: UserRepository, db_session):
    user_instance = User(id="some not existing id")
    db_session.get.return_value = None

    with pytest.raises(EntityNotFound):
        await user_repository.get(User, user_instance.id)

    db_session.get.assert_awaited_once_with(entity=User, ident=user_instance.id)


async def test_entry_repo_get_all_entries_can_successfully_get_all_entries_by_user_id(entry_repository: EntryRepository, db_session):
    user_id = "some user id"
    entry_instance = Entry(user_id=user_id)
    db_session.scalars.return_value = [entry_instance]

    actual_entries = await entry_repository.get_all_entries(user_id)

    assert actual_entries == [entry_instance]
    db_session.scalars.assert_awaited_once()
