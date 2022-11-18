# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

if __name__ == "__main__":
    result = sum(int(x) for x in str(2**15))
    print(result)

    result = sum(int(x) for x in str(2**1000))
    print(result)
