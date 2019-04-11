# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:07:52 2018

@author: Ricardo Nunes
"""

def budgeting(budget, products, wishlist):
#    ordenar dicionario
    new_products=list(products.items())
    new_products=sorted(new_products,key=valores)
    new_products=dict(new_products)
 #   new_products=products.copy()
    preco={}
    total=0
    other_list={}
    o_minimo=0
    for produto in new_products:
        if produto in wishlist:
#            print(produto)
            other_list[produto]=new_products[produto]*wishlist[produto]
            preco[produto]=new_products[produto]
    total=sum(other_list.values())
#    preco=new_products.copy()
    sim=False
    while total>budget:
        o_minimo=minimo(preco)
        other_list[o_minimo]=other_list[o_minimo]-preco[o_minimo]
        (other_list,sim)=limpar_0(other_list)
        if sim:
            del preco[o_minimo]
        
        total=sum(other_list.values())
        
    for produto in other_list:
        other_list[produto]=int(other_list[produto]/new_products[produto])
    
        
#    other_list=list(other_list.items())
#    other_list=sorted(other_list,key=asc)
#    other_list=dict(other_list)
    
    return other_list
    
def limpar_0(adict):
    sim=False
    result={}
    for key in adict:
        if adict[key]!=0:
            result[key]=adict[key]
        elif adict[key]==0:
            sim=True

    return (result,sim)

def minimo(adict):
    
    minimo=0
    for produto in adict:
        if minimo==0 or adict[produto]<minimo:
            minimo=adict[produto]
            minimo_produto=produto
    
    return minimo_produto

def valores(products):
    
    (coisa,valor)=products
    
    return valor

def asc(alist):
    print(alist)
    (coisa,valor)=alist
    
    return coisa



print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))

#é preciso ser a mesma ordem??