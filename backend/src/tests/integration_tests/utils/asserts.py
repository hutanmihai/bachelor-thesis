from typing import List

from src.models import BaseModel, Entry, User


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
    assert actual_user.username == expected_user.username
    assert actual_user.email == expected_user.email
    assert actual_user.predictions == expected_user.predictions


def assert_id_did_not_change(actual: BaseModel, expected: BaseModel):
    assert actual.id == str(expected.id)


def assert_token_response(content: dict):
    assert content["token"] is not None


def assert_base_entry_response(actual_entry: Entry, expected_entry: Entry):
    assert actual_entry.id is not None
    assert actual_entry.user_id is not None
    assert actual_entry.manufacturer == expected_entry.manufacturer
    assert actual_entry.model == expected_entry.model
    assert actual_entry.fuel == expected_entry.fuel
    assert actual_entry.chassis == expected_entry.chassis
    assert actual_entry.sold_by == expected_entry.sold_by
    assert actual_entry.gearbox == expected_entry.gearbox
    assert actual_entry.km == expected_entry.km
    assert actual_entry.power == expected_entry.power
    assert actual_entry.engine == expected_entry.engine
    assert actual_entry.year == expected_entry.year
    assert actual_entry.description == expected_entry.description
    assert actual_entry.created_at is not None
    assert actual_entry.updated_at is not None


def assert_list_entry_response(actual_entries: List[Entry], expected_entries: List[Entry]):
    for actual, expected in zip(actual_entries, expected_entries):
        assert_base_entry_response(actual, expected)
