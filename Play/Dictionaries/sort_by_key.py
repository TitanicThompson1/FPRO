# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:24:06 2018

@author: Ricardo Nunes
"""

def sort_by_key(adict):
    
    chaves=list(adict.keys())
    chaves.sort()
    valores=[]
    for chave in chaves:
        valores.append(adict.get(chave,0))
    
    return list(zip(chaves,valores))
        