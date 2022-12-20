# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

from fractions import Fraction
from functools import reduce
from operator import mul

from tqdm import tqdm


def cancel_digits(numerator: int, denominator: int) -> tuple[int, int]:
    numerator_str, denominator_str = str(numerator), str(denominator)
    for digit in range(1, 10):
        if str(digit) in numerator_str and str(digit) in denominator_str:
            numerator_str = numerator_str.replace(str(digit), "", 1)
            denominator_str = denominator_str.replace(str(digit), "", 1)

    cancelled_numerator = 0 if numerator_str == "" else int(numerator_str)
    cancelled_denominator = 0 if denominator_str == "" else int(denominator_str)

    return (cancelled_numerator, cancelled_denominator)


def can_be_digit_cancelled(numerator: int, denominator: int) -> bool:
    cancelled_numerator, cancelled_denominator = cancel_digits(numerator, denominator)

    if cancelled_denominator == 0:
        return False

    if numerator != cancelled_numerator and Fraction(numerator, denominator) == Fraction(
        cancelled_numerator, cancelled_denominator
    ):
        return True

    return False


if __name__ == "__main__":
    non_trivial_pairs: list[tuple[int, int]] = []
    for numerator in tqdm(range(10, 99)):
        for denominator in range(numerator + 1, 100):
            if not can_be_digit_cancelled(numerator, denominator):
                continue

            non_trivial_pairs.append((numerator, denominator))

    print(non_trivial_pairs)

    non_trivial_fractions = [Fraction(*pair) for pair in non_trivial_pairs]
    print(non_trivial_fractions)

    product = reduce(mul, non_trivial_fractions)
    print(product)
    print(product.denominator)
