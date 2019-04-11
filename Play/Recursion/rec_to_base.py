# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:03:15 2018

@author: Ricardo Nunes
"""

def rec_to_base(n,base):
    string="0123456789ABCDEF"
    if n<base:
        return string[n]
    else:
        return rec_to_base(n//base,base)+str(n%base)
