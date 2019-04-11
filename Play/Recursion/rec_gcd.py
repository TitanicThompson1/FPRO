# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:48:04 2018

@author: Ricardo Nunes
"""

def rec_gcd(n1, n2):
    
    if n2==0:
        return n1
    else:
        return rec_gcd(n2, n1%n2)