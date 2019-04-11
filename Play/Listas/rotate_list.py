# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:01:28 2018

@author: Ricardo Nunes
"""

def rotate_list(l):
    result=[]
    for i in range(len(l)):
        result.append(l[(i+3)%len(l)])
    return result