#!/usr/bin/env python

import itertools
import math
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
