from datetime import datetime, timezone
from uuid import UUID

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.auth.jwt_handler import token_decode
from src.database import async_session
from src.models import User


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                )
            return credentials.credentials

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = token_decode(jwtoken)
        except Exception:
            payload = None

        if payload:
            try:
                exp = payload.get("exp")
            except Exception:
                exp = None

            if not exp:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                )

            is_expired = datetime.now(timezone.utc) > datetime.fromtimestamp(exp, timezone.utc)
            if is_expired:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Expired token",
                )

            is_token_valid = True

        return is_token_valid


# Function that gets the user_id from the token after it has been decoded
async def auth_required(token: str = Depends(JWTBearer())):
    user_id = token_decode(token).get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Missing user_id in token")

    try:
        user_id = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user_id in token")

    async with async_session() as session:
        user = await session.get(User, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found, invalid token",
            )

    return user_id
