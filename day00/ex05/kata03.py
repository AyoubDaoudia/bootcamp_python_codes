#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:53:43 2021

@author: ayoub
"""
phrase = "The right format"

def kata03(text):
    print('-'*(40-len(phrase))+ phrase, end="%\n")
    
kata03(phrase)