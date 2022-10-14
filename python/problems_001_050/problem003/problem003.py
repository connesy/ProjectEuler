# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils.prime_utils import prime_factorize


print(13195, " : ", prime_factorize(13195))
print(600851475143, " : ", (factors := prime_factorize(600851475143)), "\nLargest prime factor: ", factors[-1])
