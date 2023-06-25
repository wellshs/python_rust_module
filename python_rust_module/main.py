import rust_module
import time

def time_elapsed(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        elapsed = time.time() - start
        print(f"elapsed time: {elapsed}")
        return result
    return wrapper

@time_elapsed
def python_sum_to_n(n):
    return sum(range(1, n+1))

@time_elapsed
def rust_sum_to_n(n):
    return rust_module.sum_to_n(n)


if __name__ == "__main__":
    for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        print(python_sum_to_n(n))
        print(rust_sum_to_n(n))
