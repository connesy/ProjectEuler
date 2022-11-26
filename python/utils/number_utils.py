#!/usr/bin/env python

import itertools
import math
import operator
from functools import cache
from typing import Any, Callable, Iterator


# Problem 016
def digit_sum(number: int) -> int:
    """Calculate the digit sum of a number"""
    return sum(int(d) for d in str(number))


def factorize(number: int) -> list[int]:
    """Factorize a number into all its factors, including 1 and the number itself"""
    # The following method only works when number > 3
    if number <= 3:
        return list({1, number})

    root = math.floor(math.sqrt(number))

    # Calculate all factors below the square root of number
    low_factors = [x for x in range(1, root + 1) if number % x == 0]

    # Calculate all factors above the square root of number as (number / x) for each x in low_factors.
    # If number is a perfect square, don't include same factor twice
    high_factors = [number // x for x in reversed(low_factors) if number // x != x]
    return low_factors + high_factors


@cache
def get_proper_divisors(number: int) -> list[int]:
    """Get all proper divisors for a number (numbers less than n which divide evenly into n)"""
    # The following method only works when number > 3
    if number == 1:
        return []

    factors = factorize(number)
    return factors[:-1]


def triangle_number_generator() -> Iterator[int]:
    """Return iterator over the triangle numbers, which are the sums of consecutive natural numbers"""
    return itertools.accumulate(itertools.count(2), initial=1)


def _sum_of_divisors_iterator(op: Callable[[Any, Any], bool]) -> Iterator[int]:
    for n in itertools.count(1):
        if op(sum(get_proper_divisors(n)), n):
            yield n


def perfect_number_generator() -> Iterator[int]:
    """Return iterator over the perfect numbers, which are numbers that are equal to the sum of their proper divisors"""
    yield from _sum_of_divisors_iterator(op=operator.eq)


def deficient_number_generator() -> Iterator[int]:
    """Return iterator over the deficient numbers, which are numbers where the sum of its proper divisors is
    less than the number"""
    yield from _sum_of_divisors_iterator(op=operator.lt)


def abundant_number_generator() -> Iterator[int]:
    """Return iterator over the abundant numbers, which are numbers where the sum of its proper divisors is
    more than the number"""
    yield from _sum_of_divisors_iterator(op=operator.gt)


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
