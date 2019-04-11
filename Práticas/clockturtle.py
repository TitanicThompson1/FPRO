#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:47:23 2018

@author: up201706860
"""

import turtle
wn=turtle.Screen()

ricky=turtle.Turtle()
ricky.pensize(3)
ricky.color("blue")
ricky.shape("turtle")
ricky.stamp()

for i in range(12):
    
    ricky.shape("arrow")
    ricky.penup()
    ricky.forward(100)
    ricky.pendown()
    ricky.forward(10)
    ricky.penup()
    ricky.forward(20)
    ricky.shape("turtle")
    ricky.stamp()
    ricky.forward(-130)
    ricky.left(360/12)
    
wn.mainloop()