import time
from functools import wraps

import rust_module
from matplotlib import pyplot as plt


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


if __name__ == "__main__":
    file_abs_folder_path = f"{__file__[:__file__.rfind('/')]}"
    test_input = [pow(10, i) for i in range(7)]
    test_functions = [python_sum_to_n, python_faster_sum_to_n, rust_sum_to_n]
    outputs = [[fn(n) for n in test_input] for fn in test_functions]

    # test to output is equal
    first_result = [result for result, _ in outputs[0]]
    for output in outputs:
        assert first_result == [result for result, _ in output]

    # transform elapsed time
    elapsed_dict = {
        fn.__name__: [elapsed for _, elapsed in output]
        for fn, output in zip(test_functions, outputs)
    }

    # compare elapsed time with graph
    for fn_name, elapsed in elapsed_dict.items():
        plt.plot(test_input, elapsed, label=fn_name)
    plt.yscale("log")
    plt.xscale("log")
    plt.legend()
    plt.title("sum_to_n elapsed time")
    plt.savefig(f"{file_abs_folder_path}/../images/sum_to_n_elapsed_time.png")
    plt.clf()

    # compare ratio of elapsed time python over rust
    rust_elapsed = elapsed_dict["rust_sum_to_n"]
    for fn_name, elapsed in elapsed_dict.items():
        ratio = [base / rust for base, rust in zip(elapsed, rust_elapsed)]
        plt.plot(test_input, ratio, label=fn_name)
        for i, v in enumerate(ratio):
            plt.text(test_input[i], v, "{:.2f}".format(v))

    plt.xscale("log")
    plt.legend()
    plt.title("sum_to_n elapsed time ratio")
    # plt with high resolution
    plt.savefig(f"{file_abs_folder_path}/../images/sum_to_n_elapsed_time_ratio.png")
