def get_login_payload(email: str | None, password: str | None):
    payload = {}
    if email is not None:
        payload["email"] = email
    if password is not None:
        payload["password"] = password
    return payload


def get_register_payload(email: str | None, username: str | None, password: str | None):
    payload = {}
    if email is not None:
        payload["email"] = email
    if username is not None:
        payload["username"] = username
    if password is not None:
        payload["password"] = password
    return payload


def get_inference_payload(
    manufacturer: str | None,
    model: str | None,
    fuel: str | None,
    chassis: str | None,
    sold_by: str | None,
    gearbox: str | None,
    km: int | None,
    power: int | None,
    engine: int | None,
    year: int | None,
    description: str | None,
) -> dict:
    payload = {}
    if manufacturer is not None:
        payload["manufacturer"] = manufacturer
    if model is not None:
        payload["model"] = model
    if fuel is not None:
        payload["fuel"] = fuel
    if chassis is not None:
        payload["chassis"] = chassis
    if sold_by is not None:
        payload["sold_by"] = sold_by
    if gearbox is not None:
        payload["gearbox"] = gearbox
    if km is not None:
        payload["km"] = km
    if power is not None:
        payload["power"] = power
    if engine is not None:
        payload["engine"] = engine
    if year is not None:
        payload["year"] = year
    if description is not None:
        payload["description"] = description

    return payload
