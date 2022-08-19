#!/usr/bin/python
#
# Practice Python Exercise #7
# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# 
# Let’s say I give you a list saved in a variable: 

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Write one line of Python that takes this list a and makes a new list that 
# has only the even elements of this list in it.
# ** Lesson is to learn how to make code more compact ** 

evens = [ages for ages in a if ages % 2 == 0]
print(evens)
