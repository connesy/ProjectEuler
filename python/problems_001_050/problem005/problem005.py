# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

from collections import defaultdict
import operator
import itertools
from python.utils.prime_utils import prime_factorize, prime_generator

# Solved with code (optimized brute force)
# def smallest_divisible_number(max_divisor: int) -> int:
#     # Smallest divisible number must be a multiple of all primes below max_divisor
#     primes_below_max_divisor = itertools.takewhile(lambda x: x < max_divisor, prime_generator())
#     min_factor = list(itertools.accumulate(primes_below_max_divisor, operator.mul))[-1]

#     g = (
#         n
#         for n in itertools.count(start=0, step=min_factor)
#         if all(n % divisor == 0 for divisor in range(2, max_divisor))
#     )

#     # First value is 0, second is smallest divisible number
#     next(g)
#     return next(g)


# Solved with math
def smallest_divisible_number(max_divisor: int) -> int:
    factors: dict[int, int] = defaultdict(lambda: 0)

    for divisor in range(2, max_divisor + 1):
        prime_factors = prime_factorize(divisor, as_dict=True)
        for factor, exponent in prime_factors.items():
            factors[factor] = max(factors[factor], exponent)

    iterable = (factor**exponent for factor, exponent in factors.items())
    smallest_number = list(itertools.accumulate(iterable, operator.mul))[-1]
    return smallest_number


if __name__ == "__main__":
    print(smallest_divisible_number(max_divisor=20))
