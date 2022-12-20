# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

from tqdm import tqdm

ALL_DIGITS = [str(d) for d in range(1, 10)]


def is_pandigital(multiplicant: str, multiplier: str, product: str, all_digits: list[str]) -> bool:
    """Return whether the identity multiplicand/multiplier/product is 1 through n pandigital
    (contains all numbers 1 through n)"""

    digits = list(sorted([*multiplicant, *multiplier, *product]))
    return digits == all_digits


if __name__ == "__main__":
    pandigitals: set[int] = set()
    non_repeat_digits = [x for x in range(1, 10000) if len(set(str(x))) == len(str(x))]
    for multiplicant in tqdm(non_repeat_digits):
        multiplicant_str = str(multiplicant)
        for multiplier in (x for x in non_repeat_digits if x >= multiplicant):
            if not is_pandigital(
                multiplicant=multiplicant_str,
                multiplier=str(multiplier),
                product=str(multiplicant * multiplier),
                all_digits=ALL_DIGITS,
            ):
                continue

            print(multiplicant, multiplier, multiplicant * multiplier)
            pandigitals.add(multiplicant * multiplier)

    print(pandigitals)
    print(sum(pandigitals))
