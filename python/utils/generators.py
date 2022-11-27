#!/usr/bin/env python

import itertools
import operator
from typing import Any, Callable, Iterator

from python.utils.number_utils import get_proper_divisors, nth_fibonnaci


def triangle_numbers() -> Iterator[int]:
    """Return iterator over the triangle numbers, which are the sums of consecutive natural numbers"""
    return itertools.accumulate(itertools.count(2), initial=1)


def _sum_of_divisors(op: Callable[[Any, Any], bool]) -> Iterator[int]:
    for n in itertools.count(1):
        if op(sum(get_proper_divisors(n)), n):
            yield n


def perfect_numbers() -> Iterator[int]:
    """Return iterator over the perfect numbers, which are numbers that are equal to the sum of their proper divisors"""
    yield from _sum_of_divisors(op=operator.eq)


def deficient_numbers() -> Iterator[int]:
    """Return iterator over the deficient numbers, which are numbers where the sum of its proper divisors is
    less than the number"""
    yield from _sum_of_divisors(op=operator.lt)


def abundant_numbers() -> Iterator[int]:
    """Return iterator over the abundant numbers, which are numbers where the sum of its proper divisors is
    more than the number"""
    yield from _sum_of_divisors(op=operator.gt)


def fibonacci() -> Iterator[int]:
    for n in itertools.count(1):
        yield nth_fibonnaci(n)
