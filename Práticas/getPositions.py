#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:41:07 2018

@author: up201706860
"""

def get_positions(word_list,d):
    posi=-1
    posj=-1
    for i in word_list:
        posi=posi+1
        for j in word_list:
            posj=posj+1
            if i+" "+j==d and posi!=posj:
                return str(posi)+" "+str(posj)
    
        posj=-1

print(get_positions(["hello", "brave", "world"], "hello world"))
