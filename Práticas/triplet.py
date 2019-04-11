#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:11:26 2018

@author: up201706860
"""

def triplet(atuple):
    
    for i in range(len(atuple)):
        for j in range(i+1,len(atuple)):
            for k in range(j+1,len(atuple)):
                soma=atuple[i]+atuple[j]+atuple[k]
                if soma==0:
                    return (atuple[i],atuple[j],atuple[k])
    
    return ()

