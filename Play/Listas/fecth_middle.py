# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:19:04 2018

@author: Ricardo Nunes
"""

def fetch_middle(lists):
    result=[]
    for l in lists:
        result.append(l[len(l)//2] if len(l)%2!=0 else (l[len(l)//2]+l[len(l)//2-1])/2)
    return result
        