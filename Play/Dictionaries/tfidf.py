# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:09:59 2018

@author: Ricardo Nunes
"""
import math
def tfidf(documents):
    dic={}
    indoc={}
    result={}
    nodoc={}
    allwords=[]
    n={}
    for doc in documents:
        allwords=allwords+doc.split()
    
    for doc in documents:
        adoc=doc.lower()
        lista=adoc.split()
        for word in lista:
            dic[word]=[]
    
    for doc in documents:   
        for key in dic:
            if key in doc:
                n[key]=n.get(key,0)+1
                
    print(n)
    for doc in documents: 
        adoc=doc.lower()
        lista=adoc.split()
        for word in lista:
            nodoc[word]=nodoc.get(word,0)+1
        for key in dic:
            dic[key]=dic[key]+[nodoc.get(key,0)]
            
        nodoc={}
    print(dic)
    result={}
    
    for key in dic:
        result[key]=mult(dic[key],math.log10())

    print(result)

            
    return result

tfidf(["To be or not to be", "Impossible is a word to be found only in the dictionary of fools", "There is nothing impossible to him who will try"])