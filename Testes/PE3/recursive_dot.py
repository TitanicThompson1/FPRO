# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:51:52 2019

@author: Ricardo Nunes
"""

def recursive_dot(l1, l2):
    result=0
    for i,ele in enumerate(l1):
        if type(ele)==list:
            result+=recursive_dot(ele,l2[i])
            
        else:
            result+=ele*l2[i]
    return result

