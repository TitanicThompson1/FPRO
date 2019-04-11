# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:03:30 2019

@author: Ricardo Nunes
"""

def alarm(hour,minutes):
    hora= (hour+6)%24
    minutos=(minutes+51)%60
    if (minutes+51)>59:
        hora+=(minutes+51)//60
    if minutos<10:
        minutos="0"+str(minutos)
    if hora<10:
        hora="0"+str(hora)
    
    
        
    return str(hora)+":"+str(minutos)

print(alarm(20,20))