# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import itertools

import more_itertools

if __name__ == "__main__":
    numbers = list(range(10))
    permutations = itertools.permutations(numbers)
    nth_permutation = more_itertools.nth_or_last(permutations, n=10**6 - 1)
    print(nth_permutation)
