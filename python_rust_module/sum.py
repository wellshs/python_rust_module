import time
from functools import wraps

import rust_module


def time_elapsed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        elapsed = time.time() - start
        return result, elapsed

    return wrapper


@time_elapsed
def python_sum_to_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


@time_elapsed
def python_faster_sum_to_n(n):
    return sum(range(1, n + 1))


@time_elapsed
def rust_sum_to_n(n):
    return rust_module.sum_to_n(n)
