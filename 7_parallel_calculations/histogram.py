import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np
import time


def square(a):
    return a*a


def calculate_pythagoras_histogram(num_runs):
    pythagoras = np.zeros(num_runs, dtype=float)
    for idx in range(num_runs):
        pythagoras[idx] = square(idx) + square(idx)
    y_axis = list(pythagoras)
    x_axis = list(range(0, num_runs))

    return x_axis, y_axis


def main():
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread:
        th = thread.submit(calculate_pythagoras_histogram, 1_000_000)
    x_axis, y_axis = th.result()
    end = time.time()
    print(f"with threading: {end-start}secs")

    start = time.time()
    x_axis, y_axis = calculate_pythagoras_histogram(1_000_000)
    end = time.time()
    print(f"without threading: {end-start}secs")

    # print(x_axis, y_axis)
    fig, ax = plt.subplots()
    ax.stem(x_axis, y_axis)
    plt.show()


if __name__ == '__main__':
    main()
