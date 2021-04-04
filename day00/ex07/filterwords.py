# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import string
import sys

def words_pythonest(text,n):
    words=[]
    c=""
    j=0
    while text[j].isspace():
        j+=1
    for i in range(j,len(text)):
        if text[i].isalpha():
            c+=text[i]
            if i==len(text)-1:
                words.append(c)
        else:
            if (text[i].isspace() and text[i-1].isalpha()) or (text[i] in string.punctuation):
                words.append(c)
            c=""
    words_sorted=[]
    for i in words:
        if len(i)>n:
            words_sorted.append(i)
    return words_sorted
    
if __name__=='__main__':
    if len(sys.argv)>3:
        print("Too many arguments")
    elif len(sys.argv)<3:
        print("Few arguments")
    else:
        if sys.argv[1].isdigit():
            print("ERROR")
        else:
            if sys.argv[2].isdigit():
                print(words_pythonest(sys.argv[1],int(sys.argv[2])))
            else:
                print("ERROR")