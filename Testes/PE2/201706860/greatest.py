#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:21:55 2018

@author: exame
"""

def greatest(num):
    
    list_num=list(str(num))
    list_num=sorted(list_num, reverse=True)
    first_result="".join(list_num)
    
    result=int(first_result)
    
    
    return result

