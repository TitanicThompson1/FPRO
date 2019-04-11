#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:14:44 2018

@author: up201706860
"""

n=int(input("Introduza um nº->  "))
result=""
for i in range(1,(n+1)):
    
    if i%3==0 and i%5==0:
        
        result=result+"  "
    elif i%3==0:
        
        result=result+"Fizz "
        
    elif i%5==0:
        result=result+"Buzz "
        
    else:
        result=result+str(i)+" "
        
print(result)        
        