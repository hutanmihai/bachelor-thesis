from typing import List

from src.models import BaseModel, User


def assert_api_validation_error(content: dict, expected_breaking_fields: List[str]):
    for i, _ in enumerate(expected_breaking_fields):
        assert content["detail"][i]["loc"][0] == "body"
        assert content["detail"][i]["loc"][1] == expected_breaking_fields[i]


def assert_api_path_param_validation_error(content: dict, expected_breaking_fields: List[str]):
    for i, _ in enumerate(expected_breaking_fields):
        assert content["detail"][i]["loc"][0] == "path"
        assert content["detail"][i]["loc"][1] == expected_breaking_fields[i]


def assert_api_error(content: dict, expected_description: str):
    assert content["detail"] == expected_description


def assert_http_exception_error(content: dict, expected_detail: str):
    assert content["detail"] == expected_detail


def assert_base_user_response(actual_user: User, expected_user: User):
    assert actual_user.id is not None
    assert actual_user.username == expected_user.username
    assert actual_user.email == expected_user.email
    assert actual_user.password == expected_user.password


def assert_id_did_not_change(actual: BaseModel, expected: BaseModel):
    assert actual.id == str(expected.id)
