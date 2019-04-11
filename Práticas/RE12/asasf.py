# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:48:55 2018

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
 
def transf(alist,espacos):
    result=()
    for ele in alist:
        if ele==")":
            result=(ini_result,)
            ini_result=()
        elif ele.isdigit() or "-" in ele:
            ini_result=ini_result+(ele,)
            
        else:
            
    
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