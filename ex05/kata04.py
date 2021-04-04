#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:02:35 2021

@author: ayoub
"""

def kata04():
    c=( 0, 4, 132.42222, 10000, 12345.67)
    print('day_{day}, ex_{ex} : {n1}, {n2:.2e}, {n3:.2e}'.format(day=str(c[0]).zfill(2),ex=str(c[1]).zfill(2),n1=round(c[2],2),n2=c[3],n3=c[4]))
kata04()