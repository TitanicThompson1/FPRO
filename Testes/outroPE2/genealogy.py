# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:37:40 2019

@author: Ricardo Nunes
"""

def genealogy(l):
    new_l=l.copy()
    new_l=sorted(l,key=nomes) 
    new_l=sorted(new_l,key=hier)
    return new_l

def nomes(tpl):
    a,b=tpl
    return a

def hier(tpl):
    a,b=tpl
    if b=="sibling":
        return 1
    elif b=="parent":
        return 2
    elif b=="cousin":
        return 3
    else:
        return 4
    
    