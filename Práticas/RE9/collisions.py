# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:44:24 2018

@author: Ricardo Nunes
"""

def collisions(alist):
    
    result={}
    num_hash=0
    
    for number in alist:
        
        num_hash=modul8(number)
        
        result[num_hash]= result.get(num_hash,0)+1
        
    return result

        
def modul8(number):
    
    str_number=""
    str_number=str(number)
    soma=0
    
    for digit in str_number:
        soma+=int(digit)
    
    return soma%8