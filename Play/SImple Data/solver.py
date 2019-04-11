# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:13:37 2019

@author: Ricardo Nunes
"""

def solver(a, b, c):
    result=[]
    discr=b**2-4*a*c
    if discr==0:
        result.append((0-b)/(2*a))
    elif  discr>0:
        result.append((-b-(discr**0.5))/(2*a))
        result.append((-b+(discr**0.5))/(2*a))
        result=sorted(result)
    return result
        