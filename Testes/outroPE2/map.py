# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:09:11 2019

@author: Ricardo Nunes
"""

def map(pos,steps):
    passos=steps
    passos=passos.split("-")
    x,y=pos
    for passo in passos:
        if passo=="up":
            y+=1
        if passo=="down":
            y-=1
        if passo=="left":
            x-=1
        if passo=="right":
            x+=1
    return (x,y)
            
            
        

