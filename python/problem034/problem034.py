# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""


import math

from tqdm import tqdm

FACTORIALS = [math.factorial(x) for x in range(0, 10)]


def is_equal_to_sum_of_factorials(number: int) -> bool:
    factorials = [FACTORIALS[int(digit)] for digit in str(number)]
    return sum(factorials) == number


if __name__ == "__main__":
    numbers: list[int] = []
    for number in tqdm(range(3, 1_000_001)):
        if is_equal_to_sum_of_factorials(number):
            print(number)
            numbers.append(number)

    print(sum(numbers))
