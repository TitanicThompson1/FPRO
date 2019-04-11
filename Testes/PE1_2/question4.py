# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:08:58 2019

@author: Ricardo Nunes
"""

A="rock"
B="rock"
a=A
b=B
if A=="rock":
    if B=="rock":
        result="That's a draw"
    elif B=="scissors":
        result="The winner is A"
    else:
        result="The winner is B"
elif a == "scissors":
    if b == "paper":
        print("The winner is A")
    elif b == "rock":
        print("The winner is B")
    else:
        print("That's a draw")
else:  # a == "paper"
    if b == "rock":
        print("The winner is A")
    elif b == "scissors":
        print("The winner is B")
    else:
        print("That's a draw")
        
