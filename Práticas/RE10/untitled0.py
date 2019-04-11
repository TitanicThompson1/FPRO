# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:16:41 2018

@author: Ricardo Nunes
"""

def sort_by_f(l):
    al=l.copy()
    
    al.sort(key=lambda ele: ele if ele<5 else 5-ele)
    print(al)
    return al
    