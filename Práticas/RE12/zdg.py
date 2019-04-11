# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:37:23 2018

@author: Ricardo Nunes
"""

import pdb

def parse (filename):
    
    result=[]
    
    with open(filename,"r") as f:
        f=f.readlines()

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
        
        if astring[0]=="(":
            j=1
            while espacos[j]!=espacos[0]:
                j+=1
#            pdb.set_trace()
            result=result+transf(astring[1:j],espacos[1:j]) if result!=() else (transf(astring[1:j],espacos[1:j]),)
        
        elif astring[0]==")":
                result=(result,)
        else:
            for ele in astring:
                
                result=result+(int(ele),)        
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