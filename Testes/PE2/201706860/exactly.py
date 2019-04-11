# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:37:51 2018

@author: Ricardo Nunes
"""

def exactly(s):
    
    result=()
    quest_mark=0
    numbers="0123456789"
    
    for i,letter in enumerate (s):
        
        if letter in numbers:
            
            for j,other in enumerate (s):
                
                if j>i:
                    
                    if other in numbers and (int(other)+int(letter))==10:
                        if quest_mark==3:
                            result+=(letter+other,)
                            quest_mark=0
                        
                        else:
                            
                            result+=(letter+other,)
                            return "The sequence {0} is NOT OK with first violation with pair: {1}".format(s,(letter+other,))
                
                    elif other=="?":
                        
                        quest_mark+=1
        
        quest_mark=0
    
    return "The sequence {0} is OK with the pairs: {1}".format(s,result)