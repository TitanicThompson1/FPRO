#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:22:52 2018

@author: up201706860
"""

def file_finder(dirs,file_name):
    
    path=""
    
    for subdirs in dirs:
        
        if dirs[0]== subdirs:
            path=path+subdirs+"/"
            if dirs[0]==file_name:
                path="ola"
                
        if subdirs==file_name:
            return path+file_name
        
        elif type(subdirs)==list and file_name not in path:
            if file_name in file_finder(subdirs,file_name):
                path=path +file_finder(subdirs,file_name)+"/"
                
        
    
    if "ola" in path:
        return None
    return path[:-1]

dirs = ["home",
          ["Documents",
             [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
             [ "Python", "hello_world.py", "readme.md" ],
          ],
          ["Downloads",
             [ "Movies",
                [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],
                "1.avi", "22", "001.mp4"
             ],
          ],
          "tmp.txt", "page.html"
       ]
print(file_finder(dirs,"22"))