import itertools
import math
from collections import Counter
from functools import cache
from typing import Iterator


@cache
def is_prime(number: int) -> bool:
    """Check whether a number is prime or not."""
    if number <= 0:
        return False

    if number in (1, 2):
        return True

    for divisor in range(3, math.ceil(math.sqrt(number)) + 1, 2):
        if number % divisor == 0:
            return False

    return True


def prime_generator() -> Iterator[int]:
    yield 2

    for number in itertools.count(start=3, step=2):
        if is_prime(number):
            yield number


def first_n_primes(N: int) -> Iterator[int]:
    """Return the first N primes, with the first prime being 2."""
    return itertools.islice(prime_generator(), N)


# Problem 007
def get_nth_prime(n: int) -> int:
    """Return the nth prime, with the first prime being 2."""
    return next(itertools.islice(first_n_primes(n), n - 1, None))


# Problem 010
def primes_below(N: int) -> Iterator[int]:
    """Iterator over the primes p < N."""
    return itertools.takewhile(lambda p: p < N, prime_generator())


# Problem 003
def _prime_factorize(target: int) -> list[int]:
    if target == 1:
        return []

    for prime in prime_generator():
        if target % prime == 0:
            return [prime, *prime_factorize(target=target // prime)]

    return [target]


def prime_factorize(target: int, as_dict: bool = False) -> list[int] | dict[int, int]:
    prime_factors = _prime_factorize(target=target)

    if as_dict:
        return dict(Counter(prime_factors))
    return prime_factors
