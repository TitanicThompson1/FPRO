# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 15:51:55 2018

@author: Ricardo Nunes
"""

def isomorphic(astring1, astring2):
    
    already_know={}
    
    for i,letter in enumerate(astring1):
        
        if letter not in already_know:
            
            if astring2[i] in already_know.values():
                
                return "{0} and {1} are not isomorphic".format(astring1,astring2)
            else:
                
                already_know[letter]=astring2[i]
        
        elif already_know[letter]!=astring2[i]:
            
            return "{0} and {1} are not isomorphic".format(astring1,astring2)
        
    already_know=list(already_know.items())

    
    return "{0} and {1} are isomorphic because we can map: {2}".format(astring1,astring2,already_know)

        