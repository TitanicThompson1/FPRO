#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:13:48 2018

@author: up201706860
"""

def wc(filename):
    result=()
    nlines=0
    ncharac=0
    nwords=0
    with open(filename,"r") as shakeit:
        for line in shakeit:
            nlines+=1
            
            ncharac+=len(line)
            oline=line.split()
            nwords+=len(oline)
            
    result=(nlines,nwords,ncharac)
    return result

