# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:24:32 2019

@author: Ricardo Nunes
"""

def exactly(s):
    question_marks=0
    result=()
    for i,charac in enumerate(s):
        if charac.isdigit():
            for j,o_chr in enumerate(s):
                if j>i:
                    if o_chr.isdigit() and int(o_chr)+int(charac)==10:
                        if question_marks!=3:
                            return "The sequence {0} is NOT OK with first violation with pair: {1}".format(s,(charac+o_chr,))
                        elif question_marks==3:
                            result+=(charac+o_chr,)
                    elif o_chr=="?":
                        question_marks+=1
        question_marks=0
    return "The sequence {0} is OK with the pairs: {1}".format(s,result)

                
            