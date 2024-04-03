from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src.settings import settings

async_engine = create_async_engine(settings.database_url.unicode_string(), echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncSession:
    print(settings.database_url.unicode_string())
    async with async_session() as session:
        async with session.begin():
            yield session
