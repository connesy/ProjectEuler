# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
DIGITS = set("123456789")
RECORD = 918273645


def is_pandigital(number: int) -> bool:
    number_as_string = str(number)
    return len(number_as_string) == 9 and set(number_as_string) == DIGITS


def has_repeat_digits(number: int) -> bool:
    return len(set(str(number))) < len(str(number))


def check() -> int:
    highest_number = RECORD
    for digits in (2, 3, 4):
        min_value = int(str(highest_number)[:digits])
        max_value = 10**digits
        max_products = 7 - digits

        for n in range(min_value, max_value):
            if has_repeat_digits(n):
                continue

            products = [n * i for i in range(1, max_products)]
            concatenated = int("".join(str(x) for x in products))

            if is_pandigital(concatenated):
                highest_number = max(highest_number, concatenated)

    return highest_number


if __name__ == "__main__":
    # Since we know 9 with (1,2,3,4,5) gives a solution 918273645, then a higher
    # solution would need to start with the digit 9.

    # A five-digit starting number would give a ten digit concatenated number when multiplied
    # with (1,2), so only two-, three- and four-digit numbers are candidates.

    # Two-digit starting numbers cannot reach a nine-digit concatenation by (1,2,3), since
    # "99" + "198" (99*2) + "297" (99*3) is an eight-digit number.
    # Two digit numbers also cannot use (1,2,3,4,5) since that yields ten-digit numbers.
    # So two-digit starting numbers must use (1,2,3,4).

    # Three-digit starting number cannot use (1,2) since that yields at maximum a seven-digit number.
    # (1,2,3,4) yields at least a twelve-digit number, so they must use (1,2,3).

    # Four-digit starting numbers must use (1,2), since (1,2,3) yields at least a twelve-digit number.
    print(check())
