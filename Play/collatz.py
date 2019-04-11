# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:13:59 2018

@author: Ricardo Nunes
"""

def collatz(n):
    
    result=str(n)
    
    while n!=1:
        
        if n%2==0:
            
            n=n/2
            result=result+","+str(int(n))
        
        else:
            
            n=n*3+1
            result=result+","+str(int(n))
            
    return result

