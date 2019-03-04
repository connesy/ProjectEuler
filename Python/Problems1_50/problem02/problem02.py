# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 18:27:57 2017

@author: stefan
"""

import numpy

N = 4*10**6
A = [0,1]

while A[-1] < N:
    A.append(A[-2] + A[-1])

B = A[2:-1]
print sum([x for x in B if not x % 2])