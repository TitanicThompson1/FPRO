# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:00:07 2019

@author: Ricardo Nunes
"""

number = input("Input a non negative integer: ")
prev_n=""
count=0
for n in number:
    if prev_n!="":
        if prev_n==n:
            count+=1
    prev_n=n
    
print(count)