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
