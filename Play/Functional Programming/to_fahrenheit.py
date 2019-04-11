# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:19:09 2018

@author: Ricardo Nunes
"""

def to_fahrenheit(t):
    
    result=list(map(lambda a: round(a*(9/5)+32,2),t))
    return result
