# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:42:43 2018

@author: Ricardo Nunes
"""

def sort_grades(records):
    
    records=tuple(sorted(records,key=up))
    records=tuple(sorted(records,key=name))
    records=tuple(sorted(records,key=average,reverse=True))

#    for i in range(len(records)-1):
#            
#        if average(records[i])==average(records[i+1]):
#            
#            records=records[:i]+(tuple(sorted(records[i:i+2],key=name)))+records[i+2:]
#        
#    for i in range(len(records)-1):
#            
#        if name(records[i])==name(records[i+1]):
#            
#            records=records[:i]+(tuple(sorted(records[i:i+2],key=up)))+records[i+2:]
    
    return records
    
def average(records):
    
    soma=0
    
    grades=records[2]
    
    for i in range(len(grades)):
        
        soma=soma+grades[i]
    
    media=soma/len(grades)
    
    return media

def name(records):
    
    return records[0]

def up(records):
    
    up=records[1]
    
    return int(up[2:])
    




