import numpy as np


def bubble_sort(num_to_sort: list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num_to_sort) - 1):
            if num_to_sort[i] < num_to_sort[i + 1]:
                num_to_sort[i], num_to_sort[i + 1] = num_to_sort[i + 1], num_to_sort[i]
                swapped = True
    return num_to_sort


if __name__ == "__main__":
    lists_to_sort = [
        [5, 2, 3, 1, 4],
        [-1, -8, -99, -100, -99, 124214, 1, 0],
        [0, 0, 0],
        [-1, 0, 1],
        [600, -600, 2, -2]
    ]

    cnt = 0
    for element in lists_to_sort:
        if bubble_sort(element) == sorted(element, reverse=True):
            cnt += 1
    if cnt == len(lists_to_sort):
        print("Proper implementation of custom sorting method")
    else:
        print("Wrong implementation of custom sorting method")

