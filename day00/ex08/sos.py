#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:40:07 2021

@author: ayoub
"""
import sys
import string

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def morse_characters(character):
    if character.isalnum():
        return MORSE_CODE_DICT[character.upper()]
    return ""

def morse_code(text):
    for i in range (len(text)):
        if i==len(text)-1 and text[i].isspace():
            print("")
        elif text[i].isspace() and text[i-1].isalnum():
            print("/",end=" ")
        else:
            print(morse_characters(text[i]),end=" ")
    return 

if __name__=='__main__':
    program=''
    for i in range(1,len(sys.argv)):
        program+=sys.argv[i]+" "
    for i in program:
        if i in string.punctuation:
            exit("ERROR")
    morse_code(program)

