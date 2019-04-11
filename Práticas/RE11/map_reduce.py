# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:36:31 2018

@author: Ricardo Nunes
"""
from functools import reduce
def map_reduce(n1,n2):
    prod=1
    soma=0
    result=[ele**2 for ele in range(n1,n2+1) if ele%2!=0 ]
    
    return reduce(lambda x,y: x*y if x*y<50 else x+y, result)

print( map_reduce(1,10))