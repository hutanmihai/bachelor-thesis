from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.apis.utils.utils import generate_api_error_response, generate_error_responses
from src.auth.auth_bearer import auth_required
from src.auth.jwt_handler import token_encode
from src.auth.utils import verify_password
from src.schemas.auth_schema import LoginSchema, RegisterSchema
from src.schemas.jwt_schema import TokenSchema
from src.services.errors import UserNotFound
from src.services.user_srv import UserSrv

router = APIRouter(tags=["auth"])


@router.post(
    "/register",
    summary="Register endpoint",
    status_code=status.HTTP_201_CREATED,
    response_description="User created successfully",
    responses=generate_error_responses(status.HTTP_400_BAD_REQUEST, status.HTTP_403_FORBIDDEN),
)
async def register(register_schema: RegisterSchema, user_srv: UserSrv = Depends(UserSrv)):
    username = register_schema.username
    email = register_schema.email
    password = register_schema.password

    try:
        user = await user_srv.get_user_by_email(email)
    except UserNotFound:
        user = None

    if user:
        return generate_api_error_response(status.HTTP_400_BAD_REQUEST, "User already exists")

    user = await user_srv.new_user(username, email, password)

    return TokenSchema(token=token_encode(user.id))


@router.post(
    "/login",
    summary="Login endpoint",
    status_code=status.HTTP_200_OK,
    response_description="Login successful",
    responses=generate_error_responses(status.HTTP_400_BAD_REQUEST, status.HTTP_403_FORBIDDEN),
)
async def login(login_schema: LoginSchema, user_srv: UserSrv = Depends(UserSrv)):
    email = login_schema.email
    password = login_schema.password
    try:
        user = await user_srv.get_user_by_email(email)
    except UserNotFound:
        return generate_api_error_response(status.HTTP_400_BAD_REQUEST, "Invalid credentials")

    if not await verify_password(user, password):
        return generate_api_error_response(status.HTTP_400_BAD_REQUEST, "Invalid credentials")

    return TokenSchema(token=token_encode(user.id))


@router.get(
    "/protected",
    summary="Protected endpoint for testing purposes",
    status_code=status.HTTP_200_OK,
    response_description="Protected endpoint accesed successfully",
    responses=generate_error_responses(status.HTTP_403_FORBIDDEN),
)
async def protected_return(user_id: UUID = Depends(auth_required), user_srv: UserSrv = Depends(UserSrv)):
    user = await user_srv.get_user(user_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": f"Hello {user.username} from a protected endpoint!"},
    )
