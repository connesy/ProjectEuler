# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""


def is_palindromic(target: str | int):
    target_str = str(target) if isinstance(target, int) else target
    return target_str == target_str[::-1]


if __name__ == "__main__":

    largest_palindrome: int = 0
    values: tuple[int, int] = ()
    for x in range(100, 1000):
        for y in range(x, 1000):
            product = x * y
            if product > largest_palindrome and is_palindromic(target=product):
                largest_palindrome = product
                values = (x, y)

    print(f"Largest palindrome made from two three-digit numbers {values[0], values[1]} is {largest_palindrome}")
