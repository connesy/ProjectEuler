# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
N = 4 * 10**6
fib = [0, 1]

while fib[-1] < N:
    fib.append(fib[-2] + fib[-1])

fib_even = [x for x in fib[:-1] if not x % 2]
print(sum(fib_even))
