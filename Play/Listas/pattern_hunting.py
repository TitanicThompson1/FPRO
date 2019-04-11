# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:52:16 2018

@author: Ricardo Nunes
"""

def pattern_hunting(l1, l2, p):
    result=[]
    for i in range(len(l1)):
        if p in l1[i]:
            result.append(l2[i])
        elif p in l2[i]:
            result.append(l1[i])
    
    result=sorted(result,reverse=True)
    return result

l1=['a string', 'two strings', 'not here']
p='string'
l2=['choose me', 'me too', 'but not me']
print(pattern_hunting(l1,l2,p))