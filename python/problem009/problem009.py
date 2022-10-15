# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""


def pythagorean_triplet(triplet_sum: int) -> tuple[int, int, int]:
    for c in range(3, triplet_sum - 3):
        for a in range(1, triplet_sum - c):
            b = triplet_sum - c - a
            if a**2 + b**2 == c**2:
                return a, b, c

    return (-1, -1, -1)


if __name__ == "__main__":
    a, b, c = pythagorean_triplet(triplet_sum=3 + 4 + 5)
    print(a, b, c)
    a, b, c = pythagorean_triplet(triplet_sum=1000)
    print(a, b, c)
    print(a * b * c)
