from typing import List
from uuid import UUID

from fastapi import Depends
from src.models import Entry
from src.repositories.entry_repo import EntryRepository
from src.repositories.errors import EntityNotFound
from src.repositories.user_repo import UserRepository
from src.services.abstract_srv import AbstractService
from src.services.errors import EntryNotCreatedByUser, EntryNotFound


class EntrySrv(AbstractService):
    def __init__(self, repo: UserRepository = Depends(EntryRepository)):
        super().__init__(repo)

    # Create entry
    async def create_entry(self, entry: Entry):
        await self._repository.create(entry)

    async def get_all_entries(self, user_id: UUID) -> List[Entry]:
        return await self._repository.get_all_entries(user_id)

    # Delete entry
    async def delete_entry(self, entry_id: UUID, user_id: UUID) -> None:
        try:
            instance = await self._repository.get(Entry, entry_id)
            if instance.user_id != user_id:
                raise EntryNotCreatedByUser()
            await self._repository.delete(instance)
        except EntityNotFound:
            raise EntryNotFound()
