#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:39:34 2018

@author: up201706860
"""



def remove_leading(ip):
    
    new_ip=""
    for x in ip.split(sep="."):
        
        new_ip+=str(int(x))+"."
    
    return new_ip[:-1]


