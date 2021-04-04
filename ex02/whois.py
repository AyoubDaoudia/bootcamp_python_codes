#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:29:27 2021

@author: ayoub
"""

import sys

def number(x):
    if str(x).isdigit():
        if int(x)==0:
            return "I'm zero."
        elif int(x)%2==0:
            return "I'm even."
        elif int(x)%2==1:
            return "I'm odd."
    return "ERROR"
    
if __name__=='__main__' :
    if len(sys.argv) > 2:
        print("ERROR")
    if len(sys.argv)==1:
        print("")
    else:
        print(number(sys.argv[1]))