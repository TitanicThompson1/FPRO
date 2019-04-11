# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:36:48 2018

@author: Ricardo Nunes
"""
import math

def caesar(message):
    
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    for i,letter in enumerate(message):
        
        if letter in alphabet:
            
            swift=int((((1+math.sqrt(5))**i)-((1-math.sqrt(5))**i))/((2**i)*math.sqrt(5)))
            
            new_letter=do_swift(letter,swift)
        else:
            new_letter=letter
        
        result+=new_letter
            
    return result

def do_swift(letter,swift):
    
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx=alphabet.index(letter)
    
    new_letter=alphabet[idx-swift%26]
    
    return new_letter

print(caesar("FIBONACCI SEQUENCE"))
    