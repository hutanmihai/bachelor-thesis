import bcrypt
from src.models import User


# Verify user password
async def verify_password(user: User, password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8"))


async def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()
