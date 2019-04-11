# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:45:33 2019

@author: Ricardo Nunes
"""
from math import sqrt
import string
def caesar(message):
    result=""
    punc=string.punctuation
    for i,letter in enumerate(message):
        if letter not in punc and letter!=" ":
            
            swift=((1+sqrt(5))**i-(1-sqrt(5))**i)/((2**i)*sqrt(5))
            
                
            result+=do_swift(letter,int(swift))
        else:
            result+=letter
    return result
        
def do_swift(letter,swift):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result= alphabet[alphabet.index(letter)-swift%len(alphabet)]
    return result

print(caesar("HELLO WORLD!"))