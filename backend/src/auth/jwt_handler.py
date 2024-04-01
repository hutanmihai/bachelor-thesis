from datetime import datetime, timedelta, timezone
from uuid import UUID

from jwt import decode, encode
from src.settings import settings

SECRET = settings.secret_key
ALGORITHM = settings.algorithm
EXPIRE_MINUTES = settings.access_token_expire_minutes


def token_encode(user_id: UUID) -> (str, str):
    expires = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_MINUTES)
    payload = {"exp": expires, "sub": str(user_id)}
    return encode(payload, key=SECRET, algorithm=ALGORITHM)


def token_decode(token: str) -> dict:
    return decode(token, key=SECRET, algorithms=[ALGORITHM])
