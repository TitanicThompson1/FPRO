# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:53:45 2018

@author: Ricardo Nunes
"""

def longest(s):
    
    maximo=0
    new_s=s.split()
    for x in new_s:
        if len(x)>maximo:
            maximo=len(x)
    
    return maximo

