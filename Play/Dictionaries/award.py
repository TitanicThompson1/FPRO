# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:52:23 2018

@author: Ricardo Nunes
"""

def academy_awards(alist):
    result={}
    for tpl in alist:
        award,movie=tpl
        result[movie]=result.get(movie,0)+1
    return result
        