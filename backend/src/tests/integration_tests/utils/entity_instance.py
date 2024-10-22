from typing import List

from src.auth.jwt_handler import token_encode
from src.auth.utils import hash_password
from src.database import async_session
from src.models import Entry, User
from src.tests.integration_tests.utils.data_generation_tools import get_entry_instance, get_user_instance


async def new_user() -> (User, str):
    async with async_session() as session:
        user: User = get_user_instance()
        session.add(user)
        actual_user = await session.get(User, user.id)
        await session.commit()
        token: str = token_encode(actual_user.id)
        return actual_user, token


async def new_user_with_no_predictions() -> (User, str):
    async with async_session() as session:
        user: User = get_user_instance()
        user.predictions = 0
        session.add(user)
        actual_user = await session.get(User, user.id)
        await session.commit()
        token: str = token_encode(actual_user.id)
        return actual_user, token


async def new_user_with_password(password: str) -> (User, str):
    async with async_session() as session:
        user: User = get_user_instance()
        user.password = await hash_password(password)
        session.add(user)
        actual_user = await session.get(User, user.id)
        await session.commit()
        token: str = token_encode(actual_user.id)
        return actual_user, token


async def new_entryy(user: User) -> (Entry, str):
    async with async_session() as session:
        entry: Entry = get_entry_instance(user.id)
        session.add(entry)
        actual_entry = await session.get(Entry, entry.id)
        await session.commit()
        return actual_entry


async def new_entriess(user: User, number_of_entries: int) -> List[Entry]:
    async with async_session() as session:
        entries = [get_entry_instance(user.id) for _ in range(number_of_entries)]
        session.add_all(entries)
        await session.commit()
        return entries
