#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:08:20 2018

@author: up201706860
"""

def summary_ranges(astring):
    
    list_string=astring.split(sep=",")
    ult_i=0
    result=""

    for (i,num) in enumerate (list_string):
        
        if i>0:
            
            if int(list_string[i])==(int(list_string[i-1])+1):
                
                if i==(len(list_string)-1):
                    result+=list_string[ult_i]+"->"+list_string[i]
                    
            elif (ult_i+1)==i:
                
                result+=list_string[i-1]+","
                ult_i+=1
                
                
            else:
                
                result+=list_string[ult_i]+"->"+list_string[i-1]+","
                ult_i=i
             
                if i==(len(list_string)-1):
                    result+=list_string[ult_i]
                
    return result

print (summary_ranges("0,1,2,3,4,5,7,10,11,20,21"))