# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:02:54 2019

@author: Hannah
"""

"""
Program will roll a pair of dice (number of sides will be randomly determined) 
and ask the user to guess the total value, to determine who wins

Author: Hannah
"""

from random import randint
from time import sleep

def get_sides():
  sides = randint(4, 8)
  return sides


def get_user_guess():
  guess = int(input("Make your guess: "))
  return guess


    
def roll_dice(number_of_sides):
  number_of_sides = get_sides() 
  first_roll = randint(1, number_of_sides)
  second_roll= randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print ("Maximum possible value is %d" % (max_val))
  guess = get_user_guess()
  if guess > max_val:
  	print ("Guess is too high")
  else:
    print ("Rolling...")
    sleep(2)
    print ("First roll is a %d" % (first_roll))
    sleep(2)
    print ("...and the second roll is %d" % (second_roll))
    sleep(2)
    total_roll = first_roll + second_roll
    print ("Total is... %d" % (total_roll))
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print ("Nice work! Winner!!")
    else:
      print ("Aha you lose!")

  
roll_dice(get_sides())