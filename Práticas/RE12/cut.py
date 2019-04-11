# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 18:11:03 2018

@author: Ricardo Nunes
"""

def cut(filename,delimiter,field):

    result=""
    with open(filename,"r") as f:
        for line in f:
           
            oline=line.split(delimiter)
            
            if type(field)==list:
                for index in field:
                    result+=oline[index-1]+delimiter
                result=result[:-1]
            else:
                result+=oline[field-1]
                
            
                
            result+="\n"
                
            
    return result

#print(cut("data.csv",",",2))