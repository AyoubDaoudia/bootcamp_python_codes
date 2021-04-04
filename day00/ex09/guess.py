#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 01:12:27 2021

@author: ayoub
"""
import random

print("This is an interactive guessing game!,\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")

secret=random.randint(1,99)
tries=0

while True:
    try:
        num=input("Choose a number between 1 and 99 : ")
        if num=="exit":
            print("Goodbye!")
            break
        tries+=1
        if 1<=num<=99:
            if num>secret:
                print("That is higher !")
            elif num<secret:
                print("That is lower !")
            else:
                if secret==42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                    break
                if tries==1:
                    print("Congratulations! You got it on your first try!")
                    break
                else:
                    print("Congratulations, you've got it!")
                    print("You won in {} attempts!".format(tries))
                    break
    except TypeError :
        print("That's not a number :")
    except ValueError :
        print("That's not a number :")