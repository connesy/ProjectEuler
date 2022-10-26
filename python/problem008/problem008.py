# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import numpy as np
from more_itertools import sliding_window
from python.utils.file_utils import read_data_file


def greatest_adjacent_product(number_str: str, N: int) -> int:
    """Return the greatest product of N adjacent digits in the integer represented by number_str"""
    if not number_str.isnumeric():
        raise ValueError("`number_str` must represent an integer")

    digits_iter = (int(d) for d in number_str)
    return max([int(np.prod(digits)) for digits in sliding_window(digits_iter, N)])


if __name__ == "__main__":
    number_str = "".join(read_data_file(module_file_path=__file__))
    print(greatest_adjacent_product(number_str, N=4))
    print(greatest_adjacent_product(number_str, N=13))
