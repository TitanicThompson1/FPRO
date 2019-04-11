#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:18:40 2018

@author: up201706860
"""

def manipulator (l, cmds):
    
    new_l=l[:]
    result=""
    comm_sep=[]
    for command in cmds:
        comm_sep=command.split()
        
        if len(comm_sep)==1:
            
            if command=="print":
                
                result+=str(new_l)
                result+=" " 
            elif command=="sort":
                
                new_l.sort()
                
            elif command=="pop":
                
                new_l=new_l[:-1]
                
            else:
                new_l=new_l[::-1]
                
        elif len(comm_sep)==2:
            
            if comm_sep[0]=="remove":
                
                new_l.remove(int(comm_sep[1]))
                
            else:
                new_l.append(int(comm_sep[1]))
        
        else:
            
            index=int(comm_sep[1])
            num=int(comm_sep[2])
            new_l.insert(index,num)
    
    return result[:-1]


        
                
                
        
        
                