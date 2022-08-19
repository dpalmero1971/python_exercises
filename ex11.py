#!/usr/bin/python
#
# Practice Python Exercise #11
# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
#
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to
# practice using functions.

def is_prime(help_text="Enter a number to test for primality: "):
    return int(input(help_text))