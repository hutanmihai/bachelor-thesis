from passlib.context import CryptContext
from src.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Verify user password
async def verify_password(user: User, password: str) -> bool:
    return pwd_context.verify(password, user.password)


async def hash_password(password: str) -> str:
    return pwd_context.hash(password)
