from fastapi import status
from httpx import AsyncClient
from src.tests.integration_tests.utils.asserts import assert_api_validation_error
from src.tests.integration_tests.utils.entity_instance import new_user
from src.tests.integration_tests.utils.payloads import get_inference_payload


async def test_inference_with_valid_data(client: AsyncClient):
    new_created_user, jwt = await new_user()

    request_payload = get_inference_payload(
        manufacturer="some_manufacturer",
        model="some_model",
        fuel="some_fuel",
        chassis="some_chassis",
        sold_by="some_sold_by",
        gearbox="some_gearbox",
        km=1000,
        power=100,
        engine=2000,
        year=2021,
        description="some_description",
        image_url="some_url",
    )

    expected_status_code = status.HTTP_200_OK

    response = await client.post(
        "/inference",
        json=request_payload,
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert isinstance(response.json()["prediction"], float)


async def test_inference_with_invalid_data(client: AsyncClient):
    new_created_user, jwt = await new_user()

    request_payload = get_inference_payload(
        manufacturer=None,
        model=None,
        fuel=None,
        chassis=None,
        sold_by=None,
        gearbox=None,
        km=None,
        power=None,
        engine=None,
        year=None,
        description=None,
        image_url=None,
    )

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = [
        "manufacturer",
        "model",
        "fuel",
        "chassis",
        "sold_by",
        "gearbox",
        "km",
        "power",
        "engine",
        "year",
        "description",
        "image_url",
    ]

    response = await client.post(
        "/inference",
        json=request_payload,
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), expected_breaking_fields)
