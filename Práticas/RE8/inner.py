#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:12:49 2018

@author: up201706860
"""

def inner(u,v):
    
    result=0

    for i in range(len(u)):
        
        result+=u[i]*v[i]
    
    return result

