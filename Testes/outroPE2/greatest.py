# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:21:15 2019

@author: Ricardo Nunes
"""

def greatest(num):
    anum=str(num)
    alist=list(anum)
    alist= sorted(alist, key=lambda x: int(x),reverse=True)
    return int("".join(alist))

