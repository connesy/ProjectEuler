# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils import prime_utils

if __name__ == "__main__":
    print(sum(prime_utils.primes_below(10)))
    print(sum(prime_utils.primes_below(2_000_000)))
