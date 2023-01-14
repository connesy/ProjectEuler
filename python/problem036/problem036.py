# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""


def is_palindromic_base10(number: int) -> bool:
    number_as_string = str(number)
    return number_as_string == number_as_string[::-1]


def is_palindromic_base2(number: int) -> bool:
    number_as_string = bin(number)[2:]
    return number_as_string == number_as_string[::-1]


if __name__ == "__main__":
    palindromic_numbers = (x for x in range(1_000_000) if is_palindromic_base10(x) and is_palindromic_base2(x))
    print(sum(palindromic_numbers))
