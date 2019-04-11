# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:05:02 2018

@author: Ricardo Nunes
"""

import pdb

def parse (filename):
    
    result=[]
    
    with open(filename,"r") as f:
        f=f.readlines()
#    result=limpar(f)
#    result=inteiros(result)

#    pdb.set_trace()
    espacos=[]
    espacos=conta_espacos(f)
    for ele in f:
        result.append(ele.strip())
#    pdb.set_trace()
    result=transf(result,espacos)
    
    
    return result
 
def transf(astring,espacos):
    result=()
    if len(astring)==1:
        return tuple(astring)
    else:
        
        for i,charac in enumerate(astring):
            if charac=="(" :
                j=i+1
                while espacos[j]!=espacos[i]:
                    j+=1
#                pdb.set_trace()
                result=result+transf(astring[i+1:j],espacos[i+1:j]) if result!=() else (transf(astring[i+1:j],espacos[i+1:j]),)
                
                return result
            
            elif charac==")":
                result=(result,)
                
            else:
                result=result+(int(charac),)
def limpar(alist):
    r_ele=""
    result=[]
    for ele in alist:
        for charac in ele:
            if charac!=" " and charac!="\n":
                r_ele+=charac
        result.append(r_ele)
        r_ele=""
    return result
def inteiros(alist):
    result=[]
    for ele in alist:
        if ele!="(" and ele!=")":
            result.append(int(ele))
        else:
            result.append(ele)
    return result

def conta_espacos(alist):
    count=-1
    result=[]
    for ele in alist:
        for charac in ele:
            if charac==" ":
                count+=1
        result.append(count)
        count=-1
    return result

print(parse("tuple1.txt"))