# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 22:48:33 2018

@author: Ricardo Nunes
"""

def parse (filename):
    
    result=""
    
    with open(filename,"r") as f:
        f=f.readlines()
    result=limpar(f)
    result=inteiros(result)

    result=transf(result)
    
    
    return result
 
def transf(astring):
    result=()
    if len(astring)==1:
        return tuple(astring)
    else:
        
        for i,charac in enumerate(astring):
            if charac=="(":
                if result==():
                    
                    result=((transf(astring[i+1:len(astring)-1],)),)
                else:
                    result=(result,(transf(astring[i+1:len(astring)-1],)))

                return result
            elif charac==")":
                result=(result,)
            else:
                
                result=result+(charac,)
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

print(parse("tuple2.txt"))
