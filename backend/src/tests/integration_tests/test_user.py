from fastapi import status
from httpx import AsyncClient
from src.models import User
from src.tests.integration_tests.utils.asserts import assert_api_error, assert_api_validation_error, assert_base_user_response, assert_token_response
from src.tests.integration_tests.utils.data_generation_tools import get_random_email, get_random_name
from src.tests.integration_tests.utils.entity_instance import new_user, new_user_with_password
from src.tests.integration_tests.utils.payloads import get_login_payload, get_register_payload


async def test_user_me_successfully_returns_user(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_200_OK
    expected_user = new_created_user

    response = await client.get("/user/me", headers={"Authorization": f"Bearer {jwt}"})

    assert response.status_code == expected_status_code
    assert_base_user_response(User(**response.json()), expected_user)


async def test_login_with_valid_email_and_password_successfully_logins(
    client: AsyncClient,
):
    password = "some_valid_password"
    new_created_user, jwt = await new_user_with_password(password)
    request_payload = get_login_payload(new_created_user.email, password)

    expected_status_code = status.HTTP_200_OK

    response = await client.post("/login", json=request_payload)

    assert response.status_code == expected_status_code
    assert_token_response(response.json())


async def test_login_with_invalid_email_and_invalid_password_returns_error(
    client: AsyncClient,
):
    email = "some_invalid_emaill"
    password = "no"
    request_payload = get_login_payload(email, password)

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = ["email", "password"]

    response = await client.post("/login", json=request_payload)

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), expected_breaking_fields)


async def test_register_with_valid_email_and_username_and_password_successfully_registers(
    client: AsyncClient,
):
    email = "somevalid@mail.com"
    username = "some valid username"
    password = "some_valid_password"
    request_payload = get_register_payload(email, username, password)

    expected_status_code = status.HTTP_201_CREATED

    response = await client.post("/register", json=request_payload)

    assert response.status_code == expected_status_code
    assert_token_response(response.json())


async def test_register_with_invalid_email_and_username_and_password_returns_error(client: AsyncClient):
    email = "some_invalid_email"
    username = "no"
    password = "no"
    request_payload = get_register_payload(email=email, username=username, password=password)

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = ["username", "email", "password"]

    response = await client.post("/register", json=request_payload)

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), expected_breaking_fields)


async def test_register_with_duplicate_email_returns_error(client: AsyncClient):
    new_created_user, jwt = await new_user()
    email = new_created_user.email
    username = "some valid username"
    password = "some_valid_password"
    request_payload = get_register_payload(email, username, password)

    expected_status_code = status.HTTP_400_BAD_REQUEST
    expected_description = "User already exists"

    response = await client.post("/register", json=request_payload)

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), expected_description)


async def test_login_with_bad_email_request(client: AsyncClient):
    email = get_random_email()
    password = get_random_name()

    request_payload = get_login_payload(email, password)

    expected_status_code = status.HTTP_400_BAD_REQUEST
    expected_description = "Invalid credentials"

    response = await client.post("/login", json=request_payload)

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), expected_description)


async def test_login_with_bad_password_request(client: AsyncClient):
    new_created_user, jwt = await new_user_with_password("some_valid_password")
    email = new_created_user.email
    password = "certainly_not_the_same_password"

    request_payload = get_login_payload(email, password)

    expected_status_code = status.HTTP_400_BAD_REQUEST
    expected_description = "Invalid credentials"

    response = await client.post("/login", json=request_payload)

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), expected_description)
