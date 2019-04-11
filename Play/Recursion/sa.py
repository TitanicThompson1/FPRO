# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:37:55 2019

@author: Ricardo Nunes
"""

def sum_zip(functions, arguments):
    result=[]
    aresult=[]
    if len(arguments)==0:
        return []
    for func in functions:
        result.append(list(map(func,arguments)))
        
    i=0
    temp=[]
    soma=[]
    while len(aresult)!=len(arguments):
        for ele in result:
            temp.append(ele[i])
        aresult.append(temp)
        soma.append(sum(temp))
        temp=[]
        
        i+=1
    
    result=list(zip(aresult,soma))
#    for ele in result:
#        yield ele
    return result

a=sum_zip([lambda x:x**2, lambda x:x+2], [10, 20, -5, 6, 10])
print(a)