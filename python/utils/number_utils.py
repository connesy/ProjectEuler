#!/usr/bin/env python

import itertools
import math
from functools import cache
from typing import Iterator


def factorize(number: int) -> list[int]:
    """Factorize a number into all its factors, including 1 and the number itself"""
    root = math.floor(math.sqrt(number))

    # Calculate all factors below the square root of number
    low_factors = [x for x in range(1, root) if number % x == 0]

    # Calculate all factors above the square root of number as (number / x) for each x in low_factors.
    # If number is a perfect square, don't include same factor twice
    high_factors = [number // x for x in reversed(low_factors) if number // x != x]
    return low_factors + high_factors


def triangle_number_generator() -> Iterator[int]:
    """Return iterator over the triangle numbers, which are the sums of consecutive natural numbers"""
    return itertools.accumulate(itertools.count(2), initial=1)


# Problem 014
@cache
def collatz(start: int) -> list[int]:
    """Run the Collatz sequence starting from `start` and ending with 1.

    The sequence is generated iteratively by the rules:
    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)
    """
    if start == 1:
        return [1]

    next_num = (start // 2) if (start % 2 == 0) else (3 * start + 1)
    return [start, *collatz(start=next_num)]
