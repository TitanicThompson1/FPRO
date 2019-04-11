# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:00:39 2019

@author: Ricardo Nunes
"""

def interleave(alist1, alist2):
    result=[]
    minimo=min([len(alist1),len(alist2)])
    
    for i,ele in enumerate(alist1):
        if i<minimo:
            if type(ele)==list:
                result=result+(interleave(ele,alist2[i]))
            else:
                result.append(ele)
                result.append(alist2[i])
    return result

