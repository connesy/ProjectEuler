# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

import itertools

if __name__ == "__main__":
    terms = {a**b for a, b in itertools.product(range(2, 101), range(2, 101))}
    print(len(terms))
