#!/usr/bin/python
#
# Practice Python Exercise #6
# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
#
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
# ** Moral of this lesson is that strings are lists, so you can do everything to a string
#    that you can do to a list.
#
#  Enhancements:  Ignore capitalization and punctuation, and accept full sentance palindromes.
#  Example palindromes: "radar", "123454321", "A man, a plan, a canal, Panama!", "Do geese see God?"

import re
def is_palindrome(test):

  test = re.sub(r'[^\w]','',test).lower()     # Use regex to remove punctuation marks and convert to lowercase.
  if test == (test[::-1]):
    return True
  else:
    return False
print ("Ex #6: Palindrome Test!")
pal=str(input("Enter a string to test to see if its a palindrome: "))
print (is_palindrome(pal))                    # Didn't need to use a function for this, but what-evah!