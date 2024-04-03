from random import choice as random_choice
from random import randint, random
from string import ascii_lowercase
from uuid import uuid4

from src.models import User


def generate_random_string(length: int):
    return "".join(random_choice(ascii_lowercase) for i in range(length))


def get_random_float():
    return random() * 10


def get_random_int():
    return randint(0, 10)


def generate_id():
    return str(uuid4())


def get_random_email():
    return generate_random_string(15) + "@email.com"


def get_random_name():
    return generate_random_string(15)


def get_user_instance():
    user = User()
    user.id = generate_id()
    user.username = get_random_name()
    user.email = get_random_email()
    user.password = generate_random_string(15)
    return user
