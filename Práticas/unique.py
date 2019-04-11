#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:08:11 2018

@author: up201706860
"""

def unique(atuple):
    """receives a tuple of integers and returns a tuple
with the sorted unique elements of the tuple
"""
   
    new_atuple=()
    for i in range(len(atuple)):
        if atuple[i] not in new_atuple:
                        
            new_atuple=new_atuple+(atuple[i],)
            
    new_atuple=tuple(sorted(new_atuple))
    
    return new_atuple


    
            