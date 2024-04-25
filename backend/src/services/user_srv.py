from typing import List
from uuid import UUID

from fastapi import Depends
from src.auth.utils import hash_password
from src.models import User
from src.repositories.errors import EntityNotFound, EntityNotUnique
from src.repositories.user_repo import UserRepository
from src.services.abstract_srv import AbstractService
from src.services.errors import UserAlreadyExists, UserNotFound


class UserSrv(AbstractService):
    def __init__(self, repo: UserRepository = Depends(UserRepository)):
        super().__init__(repo)

    # Get user by id
    async def get_user(self, user_id: UUID) -> User:
        try:
            return await self._repository.get(User, user_id)
        except EntityNotFound:
            raise UserNotFound()

    # Create new user in the database
    async def new_user(self, username: str, email: str, password: str) -> User:
        password = await hash_password(password)
        instance = User(username=username, email=email, password=password)
        try:
            return await self._repository.create(instance)
        except EntityNotUnique:
            raise UserAlreadyExists()

    # Get user by email
    async def get_user_by_email(self, email: str) -> User:
        try:
            return await self._repository.get_by_email(email)
        except EntityNotFound:
            raise UserNotFound()

    # Get all users
    async def get_all_users(self) -> List[User]:
        return await self._repository.list(User)

    # Delete user
    async def delete_user(self, user_id: UUID) -> None:
        try:
            instance = await self._repository.get(User, user_id)
            await self._repository.delete(instance)
        except EntityNotFound:
            raise UserNotFound()

    # Update user predictions
    async def update_user_predictions(self, user_id: UUID, predictions: int) -> User:
        try:
            instance = await self.get_user(user_id)
            instance.predictions += predictions
            return await self._repository.update(instance)
        except EntityNotFound:
            raise UserNotFound()
