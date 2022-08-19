#!/usr/bin/python
#
# Practice Python Exercise #3
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# 
#  Take a list, say for example this one:
#  
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
#   and write a program that prints out all the elements of the list that are less than 5.
#   Extras:
#   ** Instead of printing the elements one by one, make a new list that has all the elements 
#      less than 5 from this list in it and print out this new list.
#   ** Write this in one line of Python.
#   ** Ask the user for a number and return a list that contains only elements from the original
#      list a that are smaller than that number given by the user.
#
#
y=[]
z=[]                  # Have to define an empty list so we can use it later.

for i in range(len(a)):
  if a[i] < 5:
    print (a[i])      # Just print it (Original requirement)
    z.append(a[i])    # Create a new list... 
print(z)              # ...and print that out.

check = int(input("Enter a number for checking list elements:  "))
for i in range(len(a)):
  if a[i] < check:
    y.append(a[i])
print(y)

# one liner?
print ([i for i in range(len(a)) if a[i] < 5])
# Doesn't behave quite right...


