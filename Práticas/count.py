#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:19:46 2018

@author: up201706860
"""

def count(word, phrase):
    
    phrase=phrase.lower()
    word=word.lower()
    list_phrase=phrase.split()
    count=0
    
    for x in list_phrase:
        if x==word:
            count+=1
    
    return count

