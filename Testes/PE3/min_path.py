# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:06:01 2019

@author: Ricardo Nunes
"""
imp=9999999 
def min_path(matrix, a, b, visited=[]):
    if a==b:
        return 0
    elif a[0]<0 or a[1]<0 or a[0]>=len(matrix) or a[1]>=len(matrix[0]):
        return imp
    elif matrix[a[0]][a[1]]:
        return imp
    elif a in visited:
        return imp
    else:
        caminhos=[
                1+min_path(matrix,(a[0]+1,a[1]),b,visited+[a]),
                1+min_path(matrix,(a[0]+1,a[1]-1),b,visited+[a]),
                1+min_path(matrix,(a[0]+1,a[1]+1),b,visited+[a]),
                1+min_path(matrix,(a[0],a[1]+1),b,visited+[a]),
                1+min_path(matrix,(a[0],a[1]-1),b,visited+[a]),
                1+min_path(matrix,(a[0]-1,a[1]+1),b,visited+[a]),
                1+min_path(matrix,(a[0]-1,a[1]),b,visited+[a]),
                1+min_path(matrix,(a[0]-1,a[1]-1),b,visited+[a])
                ]
        return min(caminhos)

mx = [
       [False]*4,
       [False, True, False, False],
       [False, True, False, False],
       [False]*4
     ]
