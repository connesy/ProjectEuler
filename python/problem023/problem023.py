# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import itertools

from python.utils.number_utils import abundant_number_generator

MAX_LIMIT = 28123


def numbers_as_sum_of_abundant_numbers() -> set[int]:
    abundant_numbers = list(itertools.takewhile(lambda p: p <= MAX_LIMIT, abundant_number_generator()))

    sum_of_abundant_numbers = {
        x + y for i, x in enumerate(abundant_numbers) for y in abundant_numbers[i:] if y >= x and x + y <= MAX_LIMIT
    }
    return sum_of_abundant_numbers


if __name__ == "__main__":
    numbers_as_sum = numbers_as_sum_of_abundant_numbers()
    numbers_not_sum_of_abundant = [x for x in range(1, MAX_LIMIT + 1) if x not in numbers_as_sum]
    print(sum(numbers_not_sum_of_abundant))
