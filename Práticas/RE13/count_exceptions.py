# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:34:32 2019

@author: Ricardo Nunes
"""

def count_exceptions(f, n1, n2):
    count=0
    
    for num in range(n1,n2+1):
        try:
            f(num)
        except:
            count+=1
    return count
