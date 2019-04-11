# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:57:58 2018

@author: Ricardo Nunes
"""

def most_frequent(alist):
    dic={}
    
    for ele in alist:
        dic[ele]=dic.get(ele,0)+1
        vmaxi=dic[ele]
        
    nmaxi=[]
    for key in dic:
        if dic[key]>=vmaxi:
            vmaxi=dic[key]
            nmaxi.append(key)
    
    return max(nmaxi)
            
            
        
            