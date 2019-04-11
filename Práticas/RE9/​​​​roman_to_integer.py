# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:30:32 2018

@author: Ricardo Nunes
"""

def roman_to_integer(astring):
    
    value=1
    prev=1000
    result=0
    for letter in astring:
        
        value=translation(letter)
        if value<=prev:
            result+=value
        else:
            result=result-prev
            a_somar=value-prev
            result+=a_somar
        prev=value
        
    return result
    
    
def translation(charac):
    
    tabela={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
    return tabela[charac]

