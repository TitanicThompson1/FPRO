# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:57:23 2018

@author: Ricardo Nunes
"""

def rec_sum_digits(n):
    if n<10:
        return n
    else:
        return n%10+rec_sum_digits(n//10)