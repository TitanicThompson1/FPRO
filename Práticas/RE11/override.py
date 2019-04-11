# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:46:36 2018

@author: Ricardo Nunes
"""

def override (l1,l2):
    primeiros=[ele[0] for ele in l2]
    result=[ele for ele in l2]+[ele for ele in l1 if ele[0] not in primeiros]
    
    result.sort(key=lambda ele: ele[0])
    return result
