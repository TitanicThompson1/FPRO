# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:35:39 2018

@author: Ricardo Nunes
"""

def batch_norm(alist, batch_size):
    result=[]
    olist=alist.copy()
    nbatch=len(alist)/batch_size
    while nbatch>0:
        result.append(olist[:batch_size])
        olist=olist[batch_size:]
        nbatch+=-1
    
    result= list(map(lambda a: [ele-median(a) for ele in a],result ))
    return result
#    for ele in result:
#        yield ele
def median(l):
    
    new=l.copy()
    new.sort()
    
    if len(new)%2==0:
        med=(new[len(new)//2]+new[len(new)//2-1])/2
    else:
        med=new[len(new)//2]
    return med
    
    
    
print(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5))