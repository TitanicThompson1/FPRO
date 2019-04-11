#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:18:31 2018

@author: up201706860
"""

def mastermind(g1,g2,g3,c1,c2,c3):
    score=0

    if g1==c1:
        score=score+3
        
    elif g1==c2 or g1==c3:
        score=score+1
        
    if g2==c2:
        score=score+3

    elif g2==c1 or g2==c3:
        score=score+1
        
    if g3==c3:
        score=score+3

    elif g3==c1 or g3==c2:
        score= score+1
    
    return score
    
            

                
            