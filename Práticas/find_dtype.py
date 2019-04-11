#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:31:04 2018

@author: up201706860
"""

def find_dtype(atuple,data_type):
    
    new_atuple=()
    for i in range(len(atuple)):
        
        if type(atuple[i]).__name__==data_type:
            
            new_atuple=new_atuple+(atuple[i],)
            
    return new_atuple

print(find_dtype((1, 2, 3),"float"))
    

    
