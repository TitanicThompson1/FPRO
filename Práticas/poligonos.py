#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:28:50 2018

@author: up201706860
"""

import turtle
wn=turtle.Screen()

ric=turtle.Turtle()
ric.pensize(4)
for i in range(4):
    
    ric.forward(100)
    ric.left(90)
    
for i in range(3):
    
    ric.forward(100)
    ric.left(120)
    
for i in range(6):
    
    ric.forward(100)
    ric.left(180-(4*180)/6)

for i in range (8):
    
    ric.forward(100)
    ric.left(180-(6*180)/8)
      