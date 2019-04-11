# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:45:41 2018

@author: Ricardo Nunes
"""

def odd_range(start, stop, step):
    
        
    result= [i if i%2!=0 else i+1 for i in range(start,stop,step*2) ]
    
    for i in result:
        yield i

    return result