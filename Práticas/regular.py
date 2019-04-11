#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 08:49:06 2018

@author: up201706860
"""

import turtle
wn= turtle.Screen()
ricardo_junior=turtle.Turtle()

n_de_lados=int(input("Introduza o numero de lados  "))
comprimento=int(input("Comprimento do lado  "))
cor_de_lado=input("Cor de lado  ")
cor_de_fill= input ("Cor de preenchimento  ")

S= (n_de_lados-2)*180

ricardo_junior.color(cor_de_lado,cor_de_fill)
ricardo_junior.begin_fill()

for i in range(n_de_lados):
    
    ricardo_junior.left(180-(S/n_de_lados))
    ricardo_junior.forward(comprimento)
    
ricardo_junior.end_fill()

wn.mainloop()    