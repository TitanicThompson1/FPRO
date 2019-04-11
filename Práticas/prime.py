#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 08:46:58 2018

@author: up201706860
"""



n=int(input("Introduza um nº  "))

result = True

if n==1:
    
    result=False
else:
    
    for i in range(2, n):
        
        print(i, end="  ")
        
        if n%i==0:
            
            result= False
            break
    
print("\n",result)    