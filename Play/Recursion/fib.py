# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:25:30 2018

@author: Ricardo Nunes
"""


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)