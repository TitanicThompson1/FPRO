#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:58:28 2018

@author: up201706860
"""

def is_perfect(n):
    
    soma=0
    for i in range(1,n):
        if n%i==0:
            soma=soma+i
    if soma==n:
        return True
    else:
        return False
