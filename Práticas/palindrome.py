#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:51:45 2018

@author: up201706860
"""

def palindrome(astring):
    
    count=0
    for i in range(len(astring)):
        for j in range(1,len(astring)):
            if i<j:
                new_astring=astring[i:j+1]
                
                reverse=""
                for k in range((len(new_astring)-1),-1,-1):
                    
                    reverse=reverse+new_astring[k]
                    
                
                
                if reverse==new_astring:
                    count+=1
                
    result="For string '{0}': {1} palindrome substrings".format(astring,count)
    return result


print(palindrome("ababa"))