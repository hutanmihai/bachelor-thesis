from sqlalchemy.sql.expression import select
from src.models import BaseModel, User
from src.repositories.errors import EntityNotFound
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """User repository"""

    async def get_by_email(self, email):
        """Get user by email"""
        user = await self.db_session.scalar(select(User).where(User.email == email))
        if not user:
            raise EntityNotFound()
        return user
