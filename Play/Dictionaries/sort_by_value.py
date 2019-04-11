# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:30:21 2018

@author: Ricardo Nunes
"""

def sort_by_value(adict):
    
    valores=list(adict.items())
    valores.sort(key=hash_color)
    return valores
    

def hash_color(tpl):
    
    soma=0
    i,hexa=tpl
    hexa=hexa[1:]
    comp=len(hexa)-1
    for i,charac in enumerate(hexa):
        if charac.isdigit():
            soma+=int(charac)*(16**(comp-i))
        elif charac=="A":
            soma+=10*(16**(comp-i))
        elif charac=="B":
            soma+=11*(16**(comp-i))
        elif charac=="C":
            soma+=12*(16**(comp-i))
        elif charac=="D":
            soma+=13*(16**(comp-i))
        elif charac=="E":
            soma+=14*(16**(comp-i))
        elif charac=="F":
            soma+=15*(16**(comp-i))
    return soma

print(sort_by_value({"Blue":"#0000FF", "Green":"#008000", "Black":"#000000", "White":"#FFFFFF"}))