# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:10:39 2017

@author: stefan
"""

print(sum(i for i in range(1, 1000) if not i % 3 or not i % 5))
