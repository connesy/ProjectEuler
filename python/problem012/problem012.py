# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils import number_utils

if __name__ == "__main__":
    for number in number_utils.triangle_number_generator():
        factors = number_utils.factorize(number)
        print(f"{len(factors):>3d} : {number:>10d}")
        if len(factors) > 500:
            break

    print(number)
