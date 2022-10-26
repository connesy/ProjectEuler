# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import numpy as np

from python.utils.file_utils import read_data_file


def parse_data():
    data = read_data_file(module_file_path=__file__)
    data_grid = np.array([[int(s) for s in line.split(" ")] for line in data])
    return data_grid


def get_best_down(data_grid: np.ndarray, n: int) -> tuple[int, int, int]:
    best_product = (0, 0, 0)
    for row in range(0, len(data_grid) - n + 1):
        sub_grid_product = data_grid[row : row + n, :].prod(axis=0)
        best_sub_product: int = sub_grid_product.max()
        if best_sub_product > best_product[0]:
            best_product = (best_sub_product, row, sub_grid_product.argmax())

    return best_product


# def get_best_right(data_grid: np.ndarray, n: int) -> tuple[int, int, int]:
#     best_product = (0, 0, 0)
#     for col in range(0, len(data_grid) - n + 1):
#         sub_grid_product = data_grid[:, col : col + n].prod(axis=1)
#         best_sub_product: int = sub_grid_product.max()
#         if best_sub_product > best_product[0]:
#             best_product = (best_sub_product, sub_grid_product.argmax(), col)

#     return best_product


def get_best_diagonal_down(data_grid: np.ndarray, n: int) -> tuple[int, int, int]:
    best_product = (0, 0, 0)
    for row in range(0, len(data_grid) - n + 1):
        for col in range(0, len(data_grid) - n + 1):
            diag_product = data_grid[row : row + n, col : col + n].diagonal().prod()
            if diag_product > best_product[0]:
                best_product = (diag_product, row, col)

    return best_product


# def get_best_diagonal_up(data_grid: np.ndarray, n: int) -> tuple[int, int, int]:
#     best_product = (0, 0, 0)
#     for row in range(n - 1, len(data_grid)):
#         for col in range(0, len(data_grid) - n + 1):
#             diag_product = data_grid[row + n : row : -1, col : col + n].diagonal().prod()
#             if diag_product > best_product[0]:
#                 best_product = (diag_product, row, col)

#     return best_product


if __name__ == "__main__":
    data_grid = parse_data()
    print(data_grid[6:10, 8:12].diagonal())

    best_down = get_best_down(data_grid, n=4)
    # best_right = get_best_right(data_grid, n=4)
    best_right = get_best_down(data_grid.T, n=4)
    best_diag_down = get_best_diagonal_down(data_grid, n=4)
    # best_diag_up = get_best_diagonal_up(data_grid, n=4)
    best_diag_up = get_best_diagonal_down(data_grid[::-1], n=4)
    print("Down: ", best_down)
    print("Right: ", best_right)
    print("Diag down: ", best_diag_down)
    print("Diag up: ", best_diag_up)
    print()
    print(max(best_down, best_right, best_diag_down, best_diag_up))
    # print(data_grid[6:10, 15])
