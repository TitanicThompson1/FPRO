15#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:00:41 2018

@author: up201706860
"""

import turtle
wn=turtle.Screen()
wn.bgcolor("blue")
fab=turtle.Turtle()
fab.shape("circle")
fab.pensize(3)
fab.color("white")

n= int(input("Numero de lados  "))

for i in range(n):
    
    fab.forward(150)
    fab.stamp()
    fab.forward(-150)
    fab.left(360/n)
    
wn.mainloop()    