# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:49:03 2018

@author: Ricardo Nunes
"""

def pascal(n):
    
    result=""
    for linha in range(n):
        
        for coluna in range(linha+1):
            result=result+str(int(factorial(linha)/(factorial(coluna)*factorial(linha-coluna))))
            if coluna!=linha:
                result=result+" "
#        print(result)
        result=result+"\n"
    
    return result    
            

def factorial(n):
    
    if n==0:
        return 1
    else:
        
        fat=1
        for i in range(1,n+1):
            fat=fat*i
            
        return fat

