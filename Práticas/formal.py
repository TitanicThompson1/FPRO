#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:26:44 2018

@author: up201706860
"""

def formal(name):
    list_name=name.split()
    i=-1
    result=list_name[len(list_name)-1]+","
    
    for x in list_name:
        i+=1
        if i==(len(list_name)-1):
            break
        else:
            result=result+" "+x[0]+"."
        
    return result

   
        
            