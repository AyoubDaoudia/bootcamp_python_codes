#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:48:42 2021

@author: ayoub
"""

import sys
import string

def op(x,y):
    x=int(x)
    y=int(y)
    print("Sum           : ",x+y)
    print("Difference    : ",x-y)
    print("Product       : ",x*y)
    print("Division      : ",end="")
    if y==0:
        print("ERROR (div by zero)")
    else:
        print(x/y)
    print("Modulo        : ",end="")
    if y==0:
        print("ERROR (modulo by zero)")
    else:
        print(x%y)
    return

if __name__=='__main__':
    if len(sys.argv)>3:
        print("Input Error: Too many arguments.\n")
        print("Usage : python ex04.py <number1> <number2>")
        print("Example: ")
        print("\tpython ex04.py 7 5")
    elif len(sys.argv)==1:
        print("Usage : python ex04.py <number1> <number2>")
        print("Example: ")
        print("\tpython ex04.py 7 5")
    elif len(sys.argv)==2:
        print("Input Error: few arguments.\n")
    else:
        if sys.argv[1].isdigit() and sys.argv[2].isdigit(): 
            op(sys.argv[1],sys.argv[2])
        else:
             exit("Input Error: only numbers.")