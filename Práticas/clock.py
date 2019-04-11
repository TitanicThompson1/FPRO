#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:28:37 2018

@author: up201706860
"""

import datetime

now= datetime.datetime.now()
h1=now.hour
m1=now.minute

print("Now: "+str(h1)+":"+str(m1))

h2=(h1+8)%24
m2=(m1+30)%60

print("Alarm: "+str(h2)+":"+str(m2))


