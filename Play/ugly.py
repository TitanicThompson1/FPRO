# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:21:24 2018

@author: Ricardo Nunes
"""

def ugly(n):
    
    primos=""
    i=2
    while i<=n:
        
        if isprime(i) and n%i==0:
            primos=primos+str(int(i))
        i+=1
    print(primos)
    for x in primos:
        if x=="2" or x=="3" or x=="5":
            primos=primos
        else:
                return False
            
    
    return True

def isprime(n):
    
    if n==1:
        return False
    else:
        
        i=2
        while i<=n//2:
            
            if n%i==0:
                return False
            i+=1
        
        return True

print(ugly(14))

                
        