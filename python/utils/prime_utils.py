from collections import Counter
import math
import itertools
from typing import Iterator


def prime_generator() -> Iterator[int]:
    yield 2

    for number in itertools.count(start=3, step=2):
        is_prime = True
        for divisor in range(2, math.ceil(math.sqrt(number)) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield number


def first_n_primes(N: int) -> itertools.islice:
    """Return the first N primes, with the first prime being 2."""
    return itertools.islice(prime_generator(), N)


# Problem 007
def get_nth_prime(N: int) -> int:
    """Return the Nth prime, with the first prime being 2."""
    return next(itertools.islice(first_n_primes(N), N - 1, None))


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
