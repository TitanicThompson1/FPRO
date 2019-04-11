# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:31:45 2018

@author: Ricardo Nunes
"""
from functools import reduce

def map_filter_reduce(lst, f1, f2, f3):
    result=lst.copy()
    result=filter(f1,result)
    result=map(f2,result)
    result=reduce(f3,result)
    return result