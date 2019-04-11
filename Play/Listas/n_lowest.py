# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:56:40 2018

@author: Ricardo Nunes
"""

def nth_lowest(lnum, n):
    lnum.sort()
    return lnum[n-1]
