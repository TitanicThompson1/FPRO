# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:46:47 2019

@author: Ricardo Nunes
"""

def evaluate(a, x):
    result= [ele*x**i for i,ele in enumerate(a)]
    return sum(result)

    