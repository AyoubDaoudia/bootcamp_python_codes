#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 01:47:17 2021

@author: ayoub
"""
import time

def ft_progress(lst):
    status='>'
    listlst=list(lst)
    for i in lst:
        print("\r","ETA :",round(0.01*listlst[-1],2),"s [{}%]".format(round(i/10),2),"[",status," "*(20-len(status)),"]","{}/1000 |".format(i+1),"Elapsed time {}s".format(round(i*0.01,2)),end='')
        if i%50==0:
            status="="+status
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)