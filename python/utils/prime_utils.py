from collections import Counter
import math
import itertools


def prime_generator() -> int:
    yield 2

    for number in itertools.count(start=3, step=2):
        is_prime = True
        for divisor in range(2, math.ceil(math.sqrt(number)) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield number


def first_n_primes(N: int) -> list[int]:
    return list(itertools.islice(prime_generator(), N))


# Problem 003
def _prime_factorize(target: int):
    if target == 1:
        return []

    for prime in prime_generator():
        if target % prime == 0:
            return [prime, *prime_factorize(target=target // prime)]


def prime_factorize(target: int, as_dict: bool = False) -> list[int] | dict[int, int]:
    prime_factors = _prime_factorize(target=target)

    if as_dict:
        return dict(Counter(prime_factors))
    return prime_factors
