# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
from python.utils import generators

if __name__ == "__main__":
    for i, fn in enumerate(generators.fibonacci()):
        if len(str(fn)) >= 1000:
            print(i + 1, fn)
            break
