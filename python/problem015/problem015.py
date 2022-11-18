# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from functools import cache


@cache
def solve_lattice(rows: int, cols: int) -> int:
    """Find the number of routes from the top left corner to the bottom right corner of a lattice,
    moving only right and down.
    """
    if rows == 1 or cols == 1:
        return 1

    return solve_lattice(rows - 1, cols) + solve_lattice(rows, cols - 1)


if __name__ == "__main__":
    grid_size = 2
    rows = cols = grid_size + 1
    print(rows, cols, solve_lattice(rows, cols))

    grid_size = 20
    rows = cols = grid_size + 1
    print(rows, cols, solve_lattice(rows, cols))
