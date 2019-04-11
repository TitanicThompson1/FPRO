# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:17:35 2018

@author: Ricardo Nunes
"""

def is_orthogonal(mx):
    transp=[]
    temp=[]
    result=[]
    result_ele=0
    result_linha=[]
    for i,linha in enumerate(mx):
        for j in range(len(linha)):
            temp.append(mx[j][i])
        transp.append(temp)
        temp=[]
#    print(transp)
    for i,linha in enumerate(mx):
        for k in range(len(linha)):
            for j,ola in enumerate(mx):
                    
                result_ele+=mx[i][j]*transp[j][k]
                    
            result_linha.append(result_ele)
            result_ele=0
                
        result.append(result_linha)
        result_linha=[]
    
    for i,linha in enumerate(mx):
        for j in range(len(linha)):
            if i==j and result[i][j]!=1:
                return False
            elif i!=j and result[i][j]!=0:
                return False
    return True
            

print(is_orthogonal([[-2,3], [4,-1]]))