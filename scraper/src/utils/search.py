from src.constants import BASE_URL


def add_page(page: int) -> str:
    """
    Adds page query parameter to the base url
    :param page: page number
    :return: url with page query parameter
    """
    return f"{BASE_URL}&page={page}"
