# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:07:52 2019

@author: Ricardo Nunes
"""

def juggler(n, p):
    if p==0:
        return n
    else:
        if juggler(n,p-1)%2==0:
            return int(juggler(n,p-1)**0.5)
        else:
            return int(juggler(n,p-1)**1.5)
print( juggler(3,2))