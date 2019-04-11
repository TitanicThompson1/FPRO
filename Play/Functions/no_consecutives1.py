# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:22:44 2018

@author: Ricardo Nunes
"""

def  no_consecutives1(k):
    todos=gera_bin(k)
    result=list(filter(tira1,todos))
    
    return len(result)
                
    return todos

def  gera_bin(k):
    result=[]
    numbers=list(range((2**k)))
    for num in numbers:
        result.append(bin(num)[2:])
    for i,num in enumerate(result):
        while len(num)!=k:
            result[i]="0"+result[i]
            num="0"+num
            
    return result
def tira1(astring):
    for i in range(len(astring)):
        if i<len(astring)-1:
            if astring[i]=="1" and astring[i+1]=="1":
                return False
            
    return True

print(no_consecutives1(3))