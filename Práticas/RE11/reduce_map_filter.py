# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:55:29 2018

@author: Ricardo Nunes
"""
import functools

def reduce_map_filter(args):
    
    
    if type(args)==list:
        return args
    

    if type(args[2])== tuple:
        args=args[0:2]+(reduce_map_filter(args[2]),)
    
    
        
    if args[0]=="map":
        return list(map(args[1],args[2]))
    elif args[0]== "filter":
        return list(filter(args[1],args[2]))
    elif args[0]== "reduce":
        
        return functools.reduce(args[1],args[2])
        
            
