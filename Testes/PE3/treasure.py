# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:37:09 2019

@author: Ricardo Nunes
"""

def treasure(clues):
    clue=(0,0)
    result=clue
    aclues=clues.copy()
    while clue in aclues:
        result=aclues[clue]
        del aclues[clue]
        clue=result
    return result

        