# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

from python.utils import number_utils

if __name__ == "__main__":
    longest_recurring = (0, 0)
    for d in range(1, 1000):
        _, recurring_digits = number_utils.divide_with_recurring(1, d)
        num_recurring_digits = len(recurring_digits)
        if num_recurring_digits > longest_recurring[1]:
            longest_recurring = (d, num_recurring_digits)

    print(longest_recurring)
    print(number_utils.divide_with_recurring(1, longest_recurring[0]))
