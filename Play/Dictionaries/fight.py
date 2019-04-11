# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:56:16 2018

@author: Ricardo Nunes
"""

def fight(heroes, villain):
    vil=villain.copy()
    her=heroes.copy()
    for heroe in her:
        if heroe["health"]>=vil["health"] and heroe["category"]==vil["category"]:
            return "{0} defeated the villain and now has a score of {1}".format(heroe["name"],heroe["score"]+1)
        elif heroe["category"]==vil["category"]:
            vil["health"]=vil["health"]-heroe["health"]/2
    return "{0} prevailed with {1}HP left".format(vil["name"],round(vil["health"],1))

print(fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, {'name': 'King', 'health': 2000, 'category': 'S', 'score': 1}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))
        