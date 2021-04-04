#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:22:58 2021

@author: ayoub
"""

t=(3,30,2019,9,25)

print("{month}/{day}/{year} {hour}:{minute}".format(month=t[3],day=t[4],year=t[2],hour=t[0],minute=t[1]))