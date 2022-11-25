# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils.file_utils import read_data_file


def parse_data_file():
    raw_data = read_data_file(module_file_path=__file__)
    data = [[int(x) for x in line.split(" ")] for line in raw_data]
    return data


def find_best_route_sums(triangle: list[list[int]]) -> list[list[int]]:

    best_route_sums = [triangle[0]]
    for i in range(1, len(triangle)):
        row = triangle[i]
        row_above_padded = [0, *best_route_sums[i - 1], 0]
        print(row_above_padded)
        print(row)
        print()
        row_sums = [x + max(row_above_padded[i], row_above_padded[i + 1]) for i, x in enumerate(row)]
        best_route_sums.append(row_sums)

    return best_route_sums


if __name__ == "__main__":
    test_data = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]
    print("Test data:")
    best_route_sums = find_best_route_sums(test_data)
    print(best_route_sums)
    best_sum = max(best_route_sums[-1])
    print(best_sum)

    print("\n\n")
    print("Data:")
    data = parse_data_file()
    best_route_sums = find_best_route_sums(data)
    print(best_route_sums)
    best_sum = max(best_route_sums[-1])
    print(best_sum)
