# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:48:46 2018

@author: Ricardo Nunes
"""

def discard_middle(s):
    
    if len(s)<=3:
        
        return ""
    else:
        
        new_s=s[:2]+s[len(s)-2:]
        return new_s

print(discard_middle("stg"))