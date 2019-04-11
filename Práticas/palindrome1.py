#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:39:21 2018

@author: up201706860
"""


num=int(input("n1->  "))

aux=num 
reverse=""
while (aux)!=0:
    
    reverse=reverse+str(aux%10)
    aux=aux//10
    

if reverse==str(num):
    result=str(num)+" is a palindrome" 
else:
    result=str(num)+" is not a palindrome"

    
        