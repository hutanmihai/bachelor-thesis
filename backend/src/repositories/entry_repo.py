from sqlalchemy import ScalarResult
from sqlalchemy.sql.expression import select
from src.models import BaseModel, Entry, User
from src.repositories.errors import EntityNotFound
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository


class EntryRepository(SQLAlchemyRepository):
    """Entry repository"""

    async def get_all_entries(self, user_id: str) -> ScalarResult[Entry]:
        """Get user entries"""
        return await self.db_session.scalars(select(Entry).where(Entry.user_id == user_id).order_by(Entry.created_at.desc()).limit(100))
