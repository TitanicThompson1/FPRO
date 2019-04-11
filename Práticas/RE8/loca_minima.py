#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:04:33 2018

@author: up201706860
"""

def local_minima(alist,n):
    
    new_alist=[]
    minimo_local=0
    result=[]
    Do_it=True
    e_minimo=False
    count=0
    
    for (i,number) in enumerate(alist):
        
        if (i-(n//2))<0:
            
            if Do_it==False:
                count+=1
            if count==n-1:
                Do_it=True
            
            new_alist=alist[:i+(n//2)+1]
            procura_i=i
            
            (minimo_local,e_minimo)=find_minim(new_alist,n,procura_i)
            
            if e_minimo and Do_it:
                
                result.append((minimo_local,i))
                
                Do_it=False
                count=0
            
        elif (i+(n//2)+1)>len(alist):
            
            if Do_it==False:
                count+=1
            if count==n-1:
                Do_it=True
            
            new_alist=alist[i-(n//2):]
            
            procura_i=(len(new_alist)-1)-((len(alist)-1)-i)
            
            (minimo_local,e_minimo)=find_minim(new_alist,n,procura_i)
            
            if e_minimo and Do_it:
                
                result.append((minimo_local,i))
                
                Do_it=False
                
                count=0
                
        else:
            
            if Do_it==False:
                count+=1
            if count==n-1:
                Do_it=True
                
            new_alist=alist[i-(n//2):i+(n//2)+1]
            
            procura_i=n//2
            
            (minimo_local,e_minimo)=find_minim(new_alist,n,procura_i)
            
            if e_minimo and Do_it:
                result.append((minimo_local,i))
                
                Do_it=False
                count=0
    return result
            
def find_minim(alist,n,procura_i):
    
    idx=0
    minimo=alist[0]
    for number in alist:
        
        if number<=minimo:
            
            minimo=number
        idx+=1
    
        if alist[procura_i]==minimo:
            e_minimo=True
        else:
            e_minimo=False
        
    return (minimo,e_minimo)
   




