# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:53:11 2019

@author: Ricardo Nunes
"""

ints = [1, 2, 2, 3, 5, 9, 13,21, 34]
num=int(input("ola"))
menor="Less: "
maior="More: "

for i in ints:
    if i <num:
        menor+= str(i)+" "
    elif i>num:
        maior+= str(i)+" "
print(menor)
print(maior)
        