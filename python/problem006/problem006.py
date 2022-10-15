# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import numpy as np


def sum_of_squares_V1(N: int) -> int:
    """Calculate the sum of squares of the first N natural numbers"""
    return sum(x**2 for x in range(1, N + 1))


def sum_of_squares(N: int) -> int:
    """Calculate the sum of squares of the first N natural numbers"""
    integers = np.arange(1, N + 1)
    return np.sum(integers * integers)


def square_of_sum_V1(N: int) -> int:
    """Calculate the square of the sum of the first N natural numbers"""
    return sum(range(1, N + 1)) ** 2


def square_of_sum(N: int) -> int:
    """Calculate the square of the sum of the first N natural numbers

    Sum of first N integers is N * (N+1) / 2, then square that.
    """
    return (N * (N + 1)) ** 2 // 4


if __name__ == "__main__":
    N = 100
    print(sum_of_squares(N))
    print(square_of_sum(N))
    print(f"Difference: {square_of_sum(N) - sum_of_squares(N)}")
