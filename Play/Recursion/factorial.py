# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:25:29 2018

@author: Ricardo Nunes
"""

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)