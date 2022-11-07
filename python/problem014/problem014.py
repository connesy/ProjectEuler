# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from tqdm import tqdm

from python.utils.number_utils import collatz

if __name__ == "__main__":
    max_length = 0
    value = None
    for start in tqdm(range(1, 1_000_000)):
        collatz_sequence = collatz(start=start)
        if len(collatz_sequence) > max_length:
            max_length = len(collatz_sequence)
            value = start

    print(value, max_length, collatz(value))
