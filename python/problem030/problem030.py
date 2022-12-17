# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from tqdm import tqdm


def sum_of_digit_powers(number: int, power: int) -> bool:
    digits = (int(x) for x in str(number))
    digit_powers = (x**power for x in digits)
    return sum(digit_powers) == number


if __name__ == "__main__":
    power_numbers = []
    for n in tqdm(range(10, 10**6 + 1)):
        if sum_of_digit_powers(number=n, power=5):
            power_numbers.append(n)

    print(power_numbers)
    print(sum(power_numbers))
