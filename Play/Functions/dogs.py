# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:35:47 2018

@author: Ricardo Nunes
"""

def dogs(h_age):
    if h_age>21:
        d_age=2
        h_age=h_age-21
        d_age+=h_age/4
    else:
        d_age=h_age/10.5
    return 