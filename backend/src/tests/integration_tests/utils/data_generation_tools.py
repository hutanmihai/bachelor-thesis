from io import BytesIO
from random import choice as random_choice
from random import randint, random
from string import ascii_lowercase
from uuid import UUID, uuid4

from PIL import Image
from src.models import Entry, User


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


def get_random_manufacturer():
    return random_choice(["bmw", "mercedes", "audi", "toyota", "dacia"])


def get_random_model():
    return random_choice(["x5", "a4", "civic", "corolla", "logan"])


def get_random_fuel():
    return random_choice(["diesel", "gas", "hybrid"])


def get_random_chassis():
    return random_choice(["sedan", "hatchback", "suv", "coupe", "convertible"])


def get_random_sold_by():
    return random_choice(["dealer", "private"])


def get_random_gearbox():
    return random_choice(["manual", "automatic"])


def get_random_description():
    return generate_random_string(randint(300, 1000))


def generate_test_file() -> BytesIO:
    image = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = BytesIO()
    image_format = "JPEG"
    image.save(img_byte_arr, format=image_format)
    img_byte_arr.seek(0)
    return img_byte_arr


def generate_non_image_file() -> BytesIO:
    text_content = "This is a test file."
    text_byte_arr = BytesIO(text_content.encode("utf-8"))
    text_byte_arr.seek(0)
    return text_byte_arr


def get_user_instance():
    user = User()
    user.id = generate_id()
    user.username = get_random_name()
    user.email = get_random_email()
    user.password = generate_random_string(15)
    return user


def get_entry_instance(user_id: UUID):
    entry = Entry()
    entry.id = generate_id()
    entry.user_id = user_id
    entry.manufacturer = get_random_manufacturer()
    entry.model = get_random_model()
    entry.fuel = get_random_fuel()
    entry.chassis = get_random_chassis()
    entry.sold_by = get_random_sold_by()
    entry.gearbox = get_random_gearbox()
    entry.km = get_random_int()
    entry.power = get_random_int()
    entry.engine = get_random_int()
    entry.year = get_random_int()
    entry.description = get_random_description()
    entry.prediction = get_random_int()
    entry.image_url = get_random_name()
    return entry
