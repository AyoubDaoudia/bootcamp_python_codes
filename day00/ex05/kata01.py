#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:16:11 2021

@author: ayoub
"""

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

keys=list(languages.keys())
values=list(languages.values())

for i in range(len(languages)):
    print("{name} was created by {creator}".format(name=keys[i],creator=values[i]))