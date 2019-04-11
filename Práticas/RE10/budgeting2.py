# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:46:33 2018

@author: Ricardo Nunes
"""

def budgeting2(budget, products, wishlist):

    new_products=list(products.items())
    new_products=sorted(new_products,key=valores)
    new_products=dict(new_products)

    preco={}
    total=0
    other_list={}
    o_minimo=0
    for produto in new_products:
        if produto in wishlist:

            other_list[produto]=new_products[produto]*wishlist[produto]
            preco[produto]=new_products[produto]
    total=sum(other_list.values())

    sim=False
    para_max=other_list.copy()
    preco_max=preco.copy()
    while total>budget:
        o_minimo=minimo(preco)
        other_list[o_minimo]=other_list[o_minimo]-preco[o_minimo]
        (other_list,sim)=limpar_0(other_list)
        if sim:
            del preco[o_minimo]
        
        total=sum(other_list.values())
    
    
    if other_list=={}:
        other_list=para_max.copy()
        total=sum(other_list.values())
        preco=preco_max.copy()
        while total>budget:
            o_maximo=maximo(preco)
            other_list[o_maximo]=other_list[o_maximo]-preco[o_maximo]
            (other_list,sim)=limpar_0(other_list)
            if sim:
                del preco[o_maximo]
        
            total=sum(other_list.values())
        
    for produto in other_list:
        other_list[produto]=int(other_list[produto]/new_products[produto])
    
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

def maximo(adict):
    maximo=0
    for produto in adict:
        if maximo==0 or adict[produto]>maximo:
            maximo=adict[produto]
            maximo_produto=produto
    
    return maximo_produto
print (maximo({'laptop': 2000, 'jeans': 50}))
print(budgeting2(1000, {'laptop': 2000, 'jeans': 50}, {'laptop': 2,'jeans': 3}))