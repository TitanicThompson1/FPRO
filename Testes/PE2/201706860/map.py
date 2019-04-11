# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def map(pos,steps):
    
    (x,y)=pos
    list_steps=steps.split("-")
    
    for comm in list_steps:
        
        if comm=="up":
            y+=1
            
        elif comm=="left":
            x=x-1
            
        elif comm== "right":
            x+=1
            
        elif comm== "down":
            y=y-1
    
    
    return (x,y)
