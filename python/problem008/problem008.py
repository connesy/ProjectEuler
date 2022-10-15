# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import numpy as np
from more_itertools import sliding_window
from python.utils.file_utils import get_file_path


def read_data_file(filename: str) -> str:
    with get_file_path(filename, __file__).open() as file:
        return "".join(file.read().splitlines())


def greatest_adjacent_product(number_str: str, N: int) -> int:
    """Return the greatest product of N adjacent digits in the integer represented by number_str"""
    if not number_str.isnumeric():
        raise ValueError("`number_str` must represent an integer")

    digits_iter = (int(d) for d in number_str)
    return max([int(np.prod(digits)) for digits in sliding_window(digits_iter, N)])


if __name__ == "__main__":
    number_str = read_data_file("data.txt")
    print(greatest_adjacent_product(number_str, N=4))
    print(greatest_adjacent_product(number_str, N=13))
