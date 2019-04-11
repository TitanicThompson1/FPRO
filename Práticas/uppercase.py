s#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:40:43 2018

@author: up201706860
"""

def uppercase(astring):
    
    """
receives a string and returns the string
with all its characters in uppercase, 
but only if it contains at least 1 uppercase letter in the first 3
characters; otherwise the function returns the given string
    """
    
    
    Do_it=False
   
    for i in range(3):

        if astring[i]==astring[i].upper() and astring[i].upper()!= astring[i].lower():
            Do_it=True
            break
        
    if Do_it:
        return astring.upper()
    else:
        return astring

