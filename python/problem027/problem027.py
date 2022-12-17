# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import itertools

from tqdm import tqdm

from python.utils import prime_utils

# When n = 0, f(0) = 0^2 + a*0 + b, so b must be prime
B_RANGE = prime_utils.primes_below(N=1001)

# When a > 0, f(n) is only ever counting up (since b is positive), while if a < 0, f(n) is a parabola,
# which should cover more numbers.
A_RANGE = range(-1000, 0)

# When n = 1, f(1) = 1 + a + b, so -a <= b + 1 -> b >= -(a+1)
COMBINATIONS = ((a, b) for a, b in itertools.product(A_RANGE, B_RANGE) if b > 0 and b >= -(a + 1))

if __name__ == "__main__":
    max_combo = (0, 0, 0)
    for a, b in tqdm(COMBINATIONS):
        for n in itertools.count():
            f_n = n**2 + a * n + b
            if not prime_utils.is_prime(f_n):
                break

        if n + 1 > max_combo[2]:
            max_combo = (a, b, n + 1)

    print(max_combo)
    print(max_combo[0] * max_combo[1])
