from src.auth.jwt_handler import token_encode
from src.database import async_session
from src.models import User
from src.tests.integration_tests.utils.data_generation_tools import get_user_instance


async def new_user() -> (User, str):
    async with async_session() as session:
        user: User = get_user_instance()
        session.add(user)
        actual_user = await session.get(User, user.id)
        await session.commit()
        token: str = token_encode(actual_user.id)
        return actual_user, token
