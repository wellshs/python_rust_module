import time

import rust_module
from matplotlib import pyplot as plt


def time_elapsed(fn):
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
def rust_sum_to_n(n):
    return rust_module.sum_to_n(n)


if __name__ == "__main__":
    test_input = [pow(10, i) for i in range(8)]
    python_output = [python_sum_to_n(n) for n in test_input]
    rust_output = [rust_sum_to_n(n) for n in test_input]

    # test to output is equal
    python_result = [output[0] for output in python_output]
    rust_result = [output[0] for output in rust_output]
    assert python_result == rust_result

    # compare elapsed time with graph
    python_elapsed = [output[1] for output in python_output]
    rust_elapsed = [output[1] for output in rust_output]
    plt.plot(test_input, python_elapsed, label="python")
    plt.plot(test_input, rust_elapsed, label="rust")
    plt.xscale("log")
    plt.yscale("log")
    plt.title("sum_to_n elapsed time")
    plt.legend()
    plt.show()

    # compare ratio of elapsed time python over rust
    ratio = [python / rust for python, rust in zip(python_elapsed, rust_elapsed)]
    plt.plot(test_input, ratio)
    plt.xscale("log")
    for i, v in enumerate(ratio):
        plt.text(test_input[i], v, "{:.2f}".format(v))
    plt.title("sum_to_n elapsed time ratio")
    plt.show()
