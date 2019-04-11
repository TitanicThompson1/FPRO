#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 08:53:42 2018

@author: up201706860
"""

def flatten(alist):
    
    result=[]
    for ele in alist:
        if type(ele)==list:
            result+=flatten(ele)
        else:
            result.append(ele)
    return result

