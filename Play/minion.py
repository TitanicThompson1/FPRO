# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:18:31 2018

@author: Ricardo Nunes
"""

def minion(astring):
    
    consoantes="QWRTYPSDFGHJKLZXCVBNM"
    voguais="AEIOU"
    substring=""
    kevin_score=0
    Consoant=False
    already_did=""
    Vowels=True
    start_j=0
    stuart_score=0
    first=True
#    Kevin score:
    
    for i in range(len(astring)):
        
        for j in range(start_j,len(astring)):
            
            substring=astring[start_j:i+start_j]
            substring+=astring[j]
            
            if i==0 and astring[j] in voguais and astring[j] not in already_did:
                
                
                kevin_score+=count(astring[j], astring)
                already_did+=astring[j]
                if first:
                    start_j=j
                    first=False
            elif astring[j] in consoantes and Consoant and substring not in already_did:
               
                kevin_score+=count(substring, astring)
                already_did+=substring
                    
            elif astring[j] in voguais and i!=0 and Vowels and substring not in already_did:
                    
                kevin_score+=count(substring, astring)
                already_did+=substring
                
            substring=astring[0:i]
            
        already_did=""
        if Consoant:
            Consoant=False
            Vowels=True
        else:
            Vowels=False
            Consoant=True
    
    start_j=0
    Consoant=True
    Vowels=False
    first=True
#    StuartScore
            
    for i in range(len(astring)):
        
        for j in range(start_j,len(astring)):
            
            substring=astring[start_j:i+start_j]
            
            substring+=astring[j]
            
            if i==0 and astring[j] in consoantes and astring[j] not in already_did:
                
                print(astring[j]+" first")
                
                stuart_score+=count(astring[j], astring)
                already_did+=astring[j]
                if first:
                    
                    start_j=j
                    first=False
            if astring[j] in consoantes and Consoant and substring not in already_did:
                
                print(substring+" cons")
                stuart_score+=count(substring, astring)
                already_did+=substring
                    
            elif astring[j] in voguais and i!=0 and Vowels and substring not in already_did:
                    
                print(substring+" vow")
                stuart_score+=count(substring, astring)
                already_did+=substring
                
            substring=astring[0:i]
            
        already_did=""
        if Consoant:
            Consoant=False
            Vowels=True
        else:
            Vowels=False
            Consoant=True
            
            
            
    return stuart_score
                
def count(sub,astring):
    
    count=0
    for i in range(len(astring)-len(sub)+1):
        
        if astring[i:i+len(sub)]==sub:
            count+=1
    return count

print(minion("BANANA"))


            