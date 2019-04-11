# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:26:07 2018

@author: Ricardo Nunes
"""

def sparse_dot_product(dict1, dict2):
    
    soma=0
    
    for key in dict1:
        
        soma+=dict1[key]*dict2.get(key,0)
    
    return soma
 