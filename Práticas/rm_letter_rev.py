jlope#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:00:30 2018

@author: up201706860
"""


def rm_letter_rev(l, astr):
    
    result=""
    i=0
    for x in astr:
        if x not in l:
            result=result+x
            
    final_result=""
    for x in result:
        
        final_result=final_result+result[len(result)-1-i]
        i+=1
    return final_result

