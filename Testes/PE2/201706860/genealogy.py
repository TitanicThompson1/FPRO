#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:09:05 2018

@author: exame
"""

def genealogy(l):
    
    new_l=[]
    new_l=sorted(l,key=asc)
    new_l=sorted(new_l,key=relatives)
    
    return new_l

def asc(tup):
    
    return tup [0]

def relatives(tup):
    score=1
    if tup[1]=="sibling":
        score=1
    elif tup[1]=="parent":
        score=2
    elif tup[1]== "cousin":
        score=3
    elif tup[1]== "grandparent":
        score=4
    
    return score


print(genealogy([("sofia", "sibling"), ("sara", "parent"), ("bernardo","parent")]))
