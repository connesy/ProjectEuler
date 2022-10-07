# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from ...utils.utils import prime_generator


def prime_factorize(target: int):
    if target == 1:
        return []

    for prime in prime_generator():
        if target % prime == 0:
            return [prime, *prime_factorize(target=target // prime)]


print(13195, " : ", prime_factorize(13195))
print(600851475143, " : ", (factors := prime_factorize(600851475143)), "\nLargest prime factor: ", factors[-1])
