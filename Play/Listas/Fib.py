# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:03:17 2018

@author: Ricardo Nunes
"""

def fib(n):
    
    result=[0,1]
    if n<3:
        return result[:n]
    else:
        i=1
        while len(result)!=0:
            i+=1
            result.append(result[i-1]+result[i-2])
    
    return result

fib(5)