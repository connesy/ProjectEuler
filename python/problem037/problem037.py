# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

from python.utils import prime_utils


def truncations_right(number_string: str) -> list[int]:
    return [int(number_string[:n]) for n in range(1, len(number_string))]


def truncations_left(number_string: str) -> list[int]:
    return [int(number_string[n:]) for n in range(0, len(number_string))]


def truncations(number: int) -> list[int]:
    number_string = str(number)
    return sorted(truncations_right(number_string) + truncations_left(number_string))


if __name__ == "__main__":
    primes = prime_utils.prime_generator()
    truncatable_primes: list[int] = []

    while next(primes) <= 7:
        pass

    while len(truncatable_primes) < 11:
        prime = next(primes)
        prime_truncations = truncations(prime)

        # If any of the truncations are even, then they are not prime (except 2).
        # Cheaper to check than is_prime()
        if any(p % 2 == 0 for p in prime_truncations if p != 2):
            continue

        if all(prime_utils.is_prime(t) for t in prime_truncations):
            truncatable_primes.append(prime)
            print(truncatable_primes)

    print(truncatable_primes)
    print(sum(truncatable_primes))
