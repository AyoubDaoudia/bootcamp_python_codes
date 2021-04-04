#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:45:04 2021

@author: ayoub
"""
t=(19,42,21)

def strtuple(x):
    print("The {} numbers are: ".format(len(x)),end="")
    for i in range(len(x)-1):
        print(x[i],end=", ")
    print(x[len(x)-1])
    return

strtuple(t)