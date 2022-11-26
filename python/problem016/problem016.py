# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils.number_utils import digit_sum

if __name__ == "__main__":
    result = digit_sum(2**15)
    print(result)

    result = digit_sum(2**1000)
    print(result)
