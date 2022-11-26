# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils.number_utils import get_proper_divisors


def find_amicable_numbers(limit: int) -> list[int]:
    factors_sum = {n: sum(get_proper_divisors(n)) for n in range(1, limit)}
    amicable_numbers = [a for a, b in factors_sum.items() if a != b and factors_sum.get(b, -1) == a]

    return amicable_numbers


if __name__ == "__main__":
    amicable_numbers = find_amicable_numbers(limit=10000)
    print(sum(amicable_numbers))
