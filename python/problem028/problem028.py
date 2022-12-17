# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

from typing import Iterator


def number_spiral_diagonal(size: int) -> Iterator[int]:
    last_num = 1
    yield last_num
    for ring in range(1, (size + 1) // 2):
        for diagonal in range(1, 5):
            current_num = last_num + 2 * ring * diagonal
            yield current_num

        last_num = current_num


if __name__ == "__main__":
    for n in number_spiral_diagonal(size=7):
        print(n)

    print(sum(number_spiral_diagonal(size=5)))
    print(sum(number_spiral_diagonal(size=1001)))
