#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:52:46 2021

@author: ayoub
"""
import sys


def reverse(S):
    P=''
    n=len(S)
    for i in range(len(S)):
        if S[n-i-1].isalpha():
            if S[n-i-1].isupper():
                P+=S[n-1-i].lower()
            else:
                P+=S[n-1-i].upper()
        else:
            P+=S[n-1-i]
    return P

if __name__=='__main__':
    program=''
    for i in range(1,len(sys.argv)):
        program+=' '+sys.argv[i]
    print(reverse(program))