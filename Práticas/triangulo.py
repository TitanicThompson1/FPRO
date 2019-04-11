#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:24:28 2018

@author: up201706860
"""

a=int(input("a->  "))
b=int(input("b->  "))
c=int(input("c->  "))

if a+b>c and b+c>a and a+c>b:
    
    if a==b and b==c:
        print(a,b,c)
        result= "Equilateral"
    elif a!=b and b!=c and a!=c:
        result= "Scalene"
    else:
        result= "Isosceles"
else:
    result="Not a triangle"
    
        
print (result)        