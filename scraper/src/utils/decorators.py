import timeit

from src.utils.discord import send_discord_notification


def show_elapsed_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time
        print(f"Elapsed time for {func.__name__}: {elapsed_time:.2f} seconds.")
        return result

    return wrapper


def send_notification(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        send_discord_notification(f"Finished running {func.__name__}!")
        return result

    return wrapper
