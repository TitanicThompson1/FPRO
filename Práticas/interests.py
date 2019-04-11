#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:16:36 2018

@author: up201706860
"""

P=int(input("principal amount "))
r=float(input( "interest rate "))/100
n=int(input( "frequency that the interest is paid out "))
t=2

A=P*(1+(r/n))**(n*t)

print(A)