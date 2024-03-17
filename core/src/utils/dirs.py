import os


def create_dir_if_not_exists(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
