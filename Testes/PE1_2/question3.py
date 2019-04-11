# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:03:25 2019

@author: Ricardo Nunes
"""

integers = [0, 2, 9, 15, 64]
reals = [0.0, 3.2, 8.4, 15.5,128.0]
result=""
for i,num in enumerate(integers):
    result+=str(max([num,reals[i]]))+" "
print(result)