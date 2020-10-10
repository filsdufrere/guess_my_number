#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:02:52 2020

@author: tevab
"""

import random

MIN = 0
MAX = 1000

if __name__ == '__main__':
    number_to_guess = random.randint(MIN, MAX)
    print("Hey ! Try to guess a number betwwen %d and %d)!" % (MIN,MAX))
    
    while True:
        user_input = input('Your guess?')
        try:
            user_attemot = int(user_input)
            if user_attempt == number_to_guess:
                print('Fantastic,o yu could find the number I had in mind')
                break
            elif user_attempt < number_to_guess:
                print('too low')
            else: 
                print('too high')
        except ValueError:
            print('You joker ... that was not an intger')
            
            