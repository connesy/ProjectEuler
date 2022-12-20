# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

from python.utils.number_utils import digit_rotations
from python.utils.prime_utils import primes_below


def is_circular_prime(prime_rotations: set[int], all_primes: set[int]) -> bool:
    for number in prime_rotations:
        if number not in all_primes:
            return False

    return True


if __name__ == "__main__":
    primes = set(primes_below(1_000_000))
    all_primes = primes.copy()
    circular_primes: list[int] = []

    while primes:
        prime = primes.pop()
        # prime_str = str(prime)
        # rotations = {int(prime_str[mid:] + prime_str[:mid]) for mid in range(len(prime_str))}
        rotations = digit_rotations(prime)

        if is_circular_prime(rotations, all_primes):
            circular_primes.extend([*rotations])

        for number in rotations:
            primes.discard(number)

    print(list(sorted(circular_primes)))
    print()
    print(len(circular_primes))
