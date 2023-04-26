# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

import itertools
import math


def num_digits(number: int) -> int:
    """Return the number of digits in `number`"""
    return int(math.log10(number) + 1)


def find_digits(positions: list[int]) -> list[int]:
    positions_iter = iter(positions)
    position = next(positions_iter)

    digit_list: list[int] = []
    pointer = 1
    for n in itertools.count(1):
        digits = num_digits(number=n)
        if pointer <= position <= pointer + (digits - 1):
            digit = int(str(n)[position - pointer])
            digit_list.append(digit)

            try:
                position = next(positions_iter)
            except StopIteration:
                break

        pointer += digits

    return digit_list


if __name__ == "__main__":
    digits = find_digits(positions=[1, 10, 100, 1000, 10_000, 100_000, 1_000_000])
    print(digits)

    result = math.prod(digits)
    print(result)
