#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:43:15 2020

@author: mahaswetamitradeb
"""
#s = 0
#for i in range(1000):
#    if i % 3 == 0 or i % 5 == 0:
#        s += i
#print(s)


#More efficient algorithm
target = 999
def sumdivisibleby(n):
    p = target // n
    return n * ((p) * (p + 1) / 2)

print(sumdivisibleby(3) + sumdivisibleby(5) - sumdivisibleby(15))
    