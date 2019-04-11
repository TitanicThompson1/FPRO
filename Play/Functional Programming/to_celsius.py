# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:13:21 2018

@author: Ricardo Nunes
"""

def to_celsius(t):
    
    result=list(map(lambda a: round((a-32)/1.8,1),t))
    return result

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))