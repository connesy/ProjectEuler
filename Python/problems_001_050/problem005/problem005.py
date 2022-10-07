# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

import itertools


def smallest_divisible_number(max_divisor: int) -> int:
    for number in itertools.count(start=2):
        is_divisible = True
        for divisor in range(2, max_divisor + 1):
            if number % divisor != 0:
                is_divisible = False
                break

        if is_divisible:
            yield number


if __name__ == "__main__":
    print(smallest_divisible_number(max_divisor=20))
