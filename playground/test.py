#!/usr/bin/env python

import os
import random

def random_number_generator():
    number = random.randint(1, 100)
    return number


first_random_number = random_number_generator()
print first_random_number


# list
favorite_fruit = ["mangos", "peaches", "persimmons"]
for i in favorite_fruit:
    print i

# Dictionaries/maps
country_capital = {"Spain" : "Madrid", "France" : "Paris", "England" : "London"}
for k, v in country_capital.items():
    print (k, v)

for i in country_capital.itervalues():
    print i

# Making a dictionary out of two lists
cars = {}
car_make = ["Ford", "Mazda", "Honda"]
car_model = ["Mustang", "CX-5", "Civic Hatcback"]

for i in range(0,len(car_model)):
    car = {}
    car[car_make[i]] = car_model[i]
    cars.update(car)

    print cars



# Tuples -- like lists but can't be changed
first_tuple = ("run", "walk", "jog")

for i in first_tuple:
    print i
'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91x99. Find the largest palindrome
made from the product of two 3 digit numbers.

# Find the largest palindrome made from a product of two 3-digit numbers
'''

def palindrom():
    min = 100
    max = 999
    largest_palindrome = 0

    for x in range(100,999):
        for i in range(100,999):
           product = x * i
           #print product
           if (str(product) == reverse(str(product))):
               if (product > largest_palindrome):
                  largest_palindrome = product


    return largest_palindrome



def reverse(string):
    s_reversed = ""
    for i in string:
        s_reversed = i + s_reversed
        #print str

    return s_reversed


print reverse("what")

print palindrom()



