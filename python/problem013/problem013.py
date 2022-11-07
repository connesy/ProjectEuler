# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils import file_utils

if __name__ == "__main__":
    number_strings = file_utils.read_data_file(module_file_path=__file__)
    numbers = [int(number_string) for number_string in number_strings]
    number_sum = sum(numbers)
    print(number_sum)
    print(str(number_sum)[:10])
