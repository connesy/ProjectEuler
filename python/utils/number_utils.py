#!/usr/bin/env python

import math
from functools import cache


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


# Problem 021
@cache
def get_proper_divisors(number: int) -> list[int]:
    """Get all proper divisors for a number (numbers less than n which divide evenly into n)"""
    # The following method only works when number > 3
    if number == 1:
        return []

    factors = factorize(number)
    return factors[:-1]


@cache
def greatest_common_divisor(a: int, b: int, /) -> int:
    """Calculate the greatest common divisor of two integers."""
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be positive.")

    if a == 0:
        return b

    if b == 0:
        return a

    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a


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


@cache
def nth_fibonnaci(n: int) -> int:
    """Return the nth Fibonacci number, where the 1st and 2nd Fibonacci numbers are 1."""
    if n in (1, 2):
        return 1
    return nth_fibonnaci(n - 1) + nth_fibonnaci(n - 2)


def divide_with_recurring(dividend: int, divisor: int) -> tuple[str, str]:
    """Divide the dividend by the divisor and return a tuple containing the first float part, and a string of digits
    that constitutes the following recurring digits.

    Example:
        divide_with_recurring(1, 2) == ("0.5", "")   # == 0.5
        divide_with_recurring(1, 3) == ("0.", "3")    # == 0.3333
        divide_with_recurring(1, 6) == ("0.1", "6")  # == 0.1666
    """

    # Calculate the integer part first
    original_dividend = dividend
    integer_part, remainder = divmod(original_dividend, divisor)

    digits = []
    repeat_digits = []
    seen_dividends = set()
    does_repeat = False
    while (dividend := remainder * 10) != 0:
        quotient, remainder = divmod(dividend, divisor)

        if dividend in seen_dividends:
            does_repeat = True
            break

        seen_dividends.add(dividend)
        digits.append(quotient)

    if does_repeat:
        first_repeat_digit = quotient
        idx = digits.index(first_repeat_digit)
        digits, repeat_digits = digits[:idx], digits[idx:]

    float_part = f"{integer_part}.{''.join(str(d) for d in digits)}"
    recurring_part = "".join(str(d) for d in repeat_digits)
    return (float_part, recurring_part)


# Problem 035
def digit_rotations(number: int) -> set[int]:
    """Return all rotations of the digits in number."""

    number_str = str(number)
    return {int(number_str[mid:] + number_str[:mid]) for mid, _ in enumerate(number_str)}
