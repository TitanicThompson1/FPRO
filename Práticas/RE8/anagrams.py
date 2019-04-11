# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:31:41 2018

@author: Ricardo Nunes
"""

def anagram(alist):
    
    new_list=alist[:]
    grupos_anagramas=[]
    result=[]
    new_list=sorted(new_list,key=alphabetic)
    
    while len(new_list)>0:
        j=1
        grupos_anagramas.append(new_list[0])
        while j<len(new_list):

            if is_anagram(new_list[0],new_list[j]):
                grupos_anagramas.append(new_list[j])
                new_list.remove(new_list[j])
                j=j-1
            j+=1
        result.append(grupos_anagramas)
        if len(new_list)>0:
            new_list.remove(new_list[0])
        grupos_anagramas=[]
    
    return result

def is_anagram(string1,string2):

    already_tested=""
    string1=string1.lower() 
    string2=string2.lower()
    for letter in string1:
        if letter!=" ":
            if letter not in already_tested:
                if string1.count(letter)!=string2.count(letter):
                    return False
                already_tested+=letter
    
    return True
def alphabetic(astring):
    
    return astring.lower()

print(anagram(["sentence", "lives", "ten scene", "bat", "Elvis", "CE sennet"]))

                
                
