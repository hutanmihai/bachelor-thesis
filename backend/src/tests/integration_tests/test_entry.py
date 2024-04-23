from fastapi import status
from httpx import AsyncClient
from src.tests.integration_tests.utils.asserts import assert_api_error, assert_api_path_param_validation_error, assert_list_entry_response
from src.tests.integration_tests.utils.data_generation_tools import generate_id
from src.tests.integration_tests.utils.entity_instance import new_entriess, new_entryy, new_user


async def test_list_entry_successfully_returns_all_entries(client: AsyncClient):
    new_created_user, jwt = await new_user()
    new_entry_one = await new_entryy(new_created_user)
    new_entry_two = await new_entryy(new_created_user)

    expected_status_code = status.HTTP_200_OK
    expected_entries = [new_entry_two, new_entry_one]

    response = await client.get("/entry/all", headers={"Authorization": f"Bearer {jwt}"})

    assert response.status_code == expected_status_code
    assert_list_entry_response(response.json()["entries"], expected_entries)


async def test_list_entry_returns_empty_array_when_no_entries(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_200_OK
    expected_entries = []

    response = await client.get("/entry/all", headers={"Authorization": f"Bearer {jwt}"})

    assert response.status_code == expected_status_code
    assert response.json()["entries"] == expected_entries


async def test_delete_entry_successfully_deletes_entry(client: AsyncClient):
    new_created_user, jwt = await new_user()
    new_entry = await new_entryy(new_created_user)

    expected_status_code = status.HTTP_200_OK

    response = await client.delete(f"/entry/{new_entry.id}", headers={"Authorization": f"Bearer {jwt}"})

    assert response.status_code == expected_status_code


async def test_delete_entry_returns_error_when_entry_not_found(client: AsyncClient):
    new_created_user, jwt = await new_user()
    random_uuid = generate_id()

    expected_status_code = status.HTTP_404_NOT_FOUND

    response = await client.delete(f"/entry/{random_uuid}", headers={"Authorization": f"Bearer {jwt}"})

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), "Entry not found")


async def test_delete_entry_invalid_path_param_id_returns_error(client: AsyncClient):
    new_created_user, jwt = await new_user()
    invalid_id = "invalid_id"

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = ["entry_id"]

    response = await client.delete(f"/entry/{invalid_id}", headers={"Authorization": f"Bearer {jwt}"})

    assert response.status_code == expected_status_code
    assert_api_path_param_validation_error(response.json(), expected_breaking_fields)


async def test_delete_entry_returns_error_when_user_not_owner_of_entry(client: AsyncClient):
    new_created_user, jwt = await new_user()
    new_entry = await new_entryy(new_created_user)

    new_created_user2, jwt2 = await new_user()

    expected_status_code = status.HTTP_403_FORBIDDEN

    response = await client.delete(f"/entry/{new_entry.id}", headers={"Authorization": f"Bearer {jwt2}"})

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), "Entry not created by user")
