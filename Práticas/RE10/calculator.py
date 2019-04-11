#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:00:22 2018

@author: up201706860
"""

def calculator(expr):
    
    result=0
    opr=""
    if type(expr)==tuple:
        for ele in expr:
            if type(ele)==int:
                if opr=="+":
                    result+=ele
                elif opr=="*":
                    result=result*ele
                elif opr=="-":
                    result=result-ele
                else:
                    result=ele
            elif type(ele)==str:
                opr=ele
            else:
                if opr=="+":
                    result+=calculator(ele)
                elif opr=="*":
                    result=result*calculator(ele)
                elif opr=="-":
                    result=result-calculator(ele)
                else:
                    result=calculator(ele)
    else:
        return expr
    return result

