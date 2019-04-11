#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:48:02 2018

@author: up201706860
"""

def translate(astring, table):
    
    
    for i in range (len(table)):
        (caract,subs)=table[i]
        astring=astring.replace(caract, str(subs))
        
    return astring



