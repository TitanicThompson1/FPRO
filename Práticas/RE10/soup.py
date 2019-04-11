#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:06:30 2018

@author: up201706860
"""

def soup(mx, word):
    next_i=0
    next_j=0
    pos=""
    mx1=transf(mx)
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i,linha in enumerate(mx1):
        for j,letter in enumerate(linha):
            if len(word)>1 and letter==word[0]:
                
                
                pos=soup(mx1, word[1:])
                
                
            if len(word)==1 and letter==word:
                return (alphabet[i]+str(j+1))
            if pos!="":
                
                next_i=alphabet.index(pos[0])
                next_j=int(pos[1])-1
                while next_i<i-1 or next_i>i+1 or next_j<j-1 or next_j>j+1:
                    
                    mx1[next_i][next_j]="0"
                    pos=soup(mx1, word)
                    next_i=alphabet.index(pos[0])
                    next_j=int(pos[1])-1
                    
                
                    
                return (alphabet[i]+str(j+1))
                
            
    
    
                
                
                
    

mx = (('R', 'T', 'B', 'N', 'T', 'O'), 
      ('Y', 'T', 'N', 'R', 'I', 'T'), 
      ('U', 'P', 'O', 'M', 'D', 'S'), 
      ('I', 'O', 'H', 'U', 'O', 'O'), 
      ('R', 'T', 'E', 'L', 'Q', 'X'), 
      ('I', 'W', 'J', 'K', 'P', 'Z'))

def transf(mx):
    lista=[]
    result=[]
    for i,linha in enumerate(mx):
        for j,letter in enumerate(linha):
            
            result.append(letter)
            
        lista.append(result)
        result=[]
    return lista

print( soup(mx, 'RIO'))
    