#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:10:43 2018

@author: up201706860
"""

import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.pensize(5)

for i in range(4):
    
    tess.forward(90)
    tess.left(90)

wn.mainloop()