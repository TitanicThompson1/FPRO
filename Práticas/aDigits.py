#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:03:36 2018

@author: up201706860
"""

def adigits(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    frst=0
    scnd=0
    trd=0
    if a>b and a>c:
        frst=a
        if b>c:
            scnd=b
            trd=c
        else:
            scnd=c
            trd=b
        
        return (frst*100+scnd*10+trd)
    
    elif b>a and b>c:
        
        frst=b
        if a>c:
            scnd=a
            trd=c
            
        else:
            scnd=c
            trd=a
        return (frst*100+scnd*10+trd)
    else:
        frst=c
        if a>b:
            scnd=a
            trd=b
        else:
            scnd=b
            trd=a
        return (frst*100+scnd*10+trd)
    
    
