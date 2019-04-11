# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:22:10 2018

@author: Ricardo Nunes
"""

def rearrange(l):
    result=[ele for ele in l if ele<=0]
#    if 0 in l:
#        result.append(0)
    result=result+[ele for ele in l if ele>0]
    return result

