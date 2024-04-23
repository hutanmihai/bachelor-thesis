from uuid import UUID

from fastapi import APIRouter, Depends, status
from src.apis.utils.utils import generate_api_error_response, generate_error_responses
from src.auth.auth_bearer import auth_required
from src.schemas.errors_schema import ApiError
from src.schemas.user_schema import UserSchema
from src.services.errors import UserNotFound
from src.services.user_srv import UserSrv

router = APIRouter(tags=["user"])


@router.get(
    "/user/me",
    summary="Get current user details",
    status_code=status.HTTP_200_OK,
    response_description="Succesfully fetched current user details",
    response_model=UserSchema,
    responses=generate_error_responses(status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN),
)
async def user_me(user_id: UUID = Depends(auth_required), user_srv: UserSrv = Depends(UserSrv)):
    try:
        user = await user_srv.get_user(user_id)
    except UserNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "User not found")
    return UserSchema(email=user.email, username=user.username, predictions=user.predictions)
