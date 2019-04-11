#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:11:14 2018

@author: up201706860
"""

def palindrome_index(s):
    
    if palindrome(s):
        return-1
        
    for i in range(len(s)):
        
        if i==0:
            if palindrome(s[i+1:]):
                return i
        
        elif i==(len(s)-1):
                if palindrome(s[:i-1]):
                    return i
                
        else:
            if palindrome((s[:i]+s[i+1:])):
                return i
        
    return -1
        
        
def palindrome(s):
    
    new_s=""
    for i in range(1,len(s)+1):
        new_s=new_s+s[-i]
    
    if new_s==s:
        return True
    else:
        return False
    
