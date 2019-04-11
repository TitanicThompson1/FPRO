# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:09:17 2019

@author: Ricardo Nunes
"""

def avg(marks):
    assert len(marks) != 0, "Lolada"
    return sum(marks)/len(marks)


# tests
print()
mark2 = [55, 88, 78, 90, 79]
print("Average of mark2:", avg(mark2))

mark1 = []
print("Average of mark1:", avg(mark1))