#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:12:48 2018

@author: up201706860
"""

def mult(M,N):
    
    result=[]
    result_linha=[]
    result_ele=0
    lin_M=len(M)
    col_M=len(M[0])
    lin_N=len(N)
    col_N=len(N[0])
    
    if col_M==lin_N:
        
        for i in range(lin_M):
            for k in range(col_N):
                for j in range(lin_N):
                    
                    result_ele+=M[i][j]*N[j][k]
                    
                result_linha.append(result_ele)
                result_ele=0
                
            result.append(result_linha)
            result_linha=[]
    
        return result
    else:
        return []

