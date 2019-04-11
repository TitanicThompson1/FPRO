# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:34:32 2019

@author: Ricardo Nunes
"""

def exception_str(f):
    try:
        
        f()
        
    except ZeroDivisionError:
        
        return("division by zero")
        
    except FileNotFoundError :
        
        return "[Errno 2] No such file or directory: {0}".format(f())
    except IndexError:
        
        return 'list index out of range'
        
    else:
        return("No exception was raised")
