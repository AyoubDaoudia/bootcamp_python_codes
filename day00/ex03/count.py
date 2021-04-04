#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:12:46 2021

@author: ayoub
"""

#import sys
import string

def text_analyzer(*text):
    """This function counts the number of characters totally, and displays the upper, lower, puctuation characters and spaces."""
    if len(text)>1:
        return "Error"
    print(type(text[0]))
    if type(text[0])!=str:
        return "ERROR"
    u=0;l=0;p=0;s=0;c=0
    for i in text[0]:
        if i.isupper(): u+=1
        elif i.islower(): l+=1
        elif i in string.punctuation: p+=1
        elif i.isspace(): s+=1
        c+=1
    print("This text contains ", c," characters:\n")
    print("- ",u," uppercase letter(s).")
    print("- ",l," lowercase letter(s).")
    print("- ",p," punctuation mark(s).")
    print("- ",s," space(s).")
    return
