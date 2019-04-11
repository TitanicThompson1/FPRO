#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:53:47 2018

@author: up201706860
"""

def rangoli(N):
    
    wide=4*N-3
    lenght=2*N-1
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet=alphabet[:N]+(N-1)*"-"
    resultlinha=""
    result=""
    
    for i in range((lenght+1)//2):
        
        for j in range((wide+1)//2):
           
            if j%2==0:
                resultlinha+=alphabet[int(-i-(j/2))-1]
                result+=alphabet[int(-i-(j/2))-1]
                
            else:
                resultlinha+="-"
                result+="-"
        
        
        umastring=resultlinha[::-1]
        result+=umastring[1:]
        result+="\n"
        resultlinha=""
    
    
    for i in range(((lenght+1)//2)-2,-1,-1):
        
        for j in range((wide+1)//2):
           
            if j%2==0:
                resultlinha+=alphabet[int(-i-(j/2))-1]
                result+=alphabet[int(-i-(j/2))-1]
                
            else:
                resultlinha+="-"
                result+="-"
        
        umastring=resultlinha[::-1]
        result+=umastring[1:]
        result+="\n"
        resultlinha=""
   
    return result
        
print(rangoli(25))