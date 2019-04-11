# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:22:55 2018

@author: Ricardo Nunes
"""
#import pdb
def sort_by_field (filename,field):
    
    with open(filename,"r") as f:
        f=f.read()
    lista2=[]
    result=[]
    final=""
    f=f.split("\n")
    for line in f:
        linha=line.split(",")
        lista2.append(tuple(linha))
#    pdb.set_trace()
    index=-1
    i=0
    while index==-1:
        if lista2[0][i]==field:
            index=i
        i+=1
        
    for ele in lista2[0]:
        final+=str(ele)+","
    
    final=final[:-1]+"\n"
    
    result=sorted(lista2[1:],key=lambda x:x[index])
    for ele1 in result:
        for ele2 in ele1:
            
            final=final+str(ele2)+","
        final=final[:-1]+"\n"
    return final
    

