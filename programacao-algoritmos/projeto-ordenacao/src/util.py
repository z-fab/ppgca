import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() * 1000
        result = func(*args, **kwargs)
        end_time = time.time() * 1000
        return (result, round(end_time - start_time, 4))

    return wrapper
