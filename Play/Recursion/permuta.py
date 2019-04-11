# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:59:27 2018

@author: Ricardo Nunes
"""


def permuta(alist1, step=0):
    alist=alist1.copy()
    result=[]
    if step == len(alist) - 1:
        return alist
    else:
        for j in range(step, len(alist)):
            alist[step], alist[j] = alist[j], alist[step]
            
            result.append(permuta(alist, step=step+1))
            alist[step], alist[j] = alist[j], alist[step]
            

        return result
print(permuta(['A', 'B', 'C']))