#!/usr/bin/python
#
# Practice Python Exercise #5
# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# New Edit, for the sake of GIT / edit 1
# Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

# and write a program that returns a list that contains only the elements that are 
# common between the lists (without duplicates). Make sure your program works on two
# lists of different sizes.
# Extras:
# ** Randomly generate two lists to test this
# ** Write this in one line of Python
print ("Welcome to exercise 5: List Overlaps.")
print ("First iteration is with predefined lists called 'a' and 'b':")
if len(a) >= len(b):
  for i in range(len(b)):
    if b[i] in a:
      if b[i] not in c:     # Have to make sure we aren't duplicating a number that is already in our c list.
        c.append(b[i])
else:
  for i in range(len(a)):
    if a[i] in b:
      if a[i] not in c:     # Have to make sure we aren't duplicating a number that is already in our c list.
        c.append(a[i])

# print(set(c))             # Probably cheaty to use a set to print only the unique values
print ("List A:",a)
print ("List B:",b)
print ("Overlaps:",c)

# Generate two lists of a random length, with random numbers in it
# and print a list that has the overlaps between the two lists.

#Create 3 empty lists
x = []
y = []
z = []

import random               # Needed for random numbers

def gen_r_list(stop, start=0):        # Function to generate a list of varying sizes, composed of random numbers 0-10. 
  iter=start
  while iter <= stop:
    yield random.randint(0,10)
    iter += 1

size1 = random.randint(5,15)          # Get a random size for the first list x[]
size2 = random.randint(5,15)          # Get a random size for the second list y[]
while size2 == size1:                 # Make sure the second list, y[], is not equal in size to x[]
  size2 = random.randint(5,15)
  print (size1, size2)

x = list(gen_r_list(size1))
y = list(gen_r_list(size2))

# Now that we've created both lists, lets create a list of overlapping values

if len(x) >= len(y):
  for i in range(len(y)):
    if y[i] in x:
      if y[i] not in z:     # Have to make sure we aren't duplicating a number that is already in our z list.
        z.append(y[i])
else:
  for i in range(len(x)):
    if x[i] in y:
      if x[i] not in z:     # Have to make sure we aren't duplicating a number that is already in our z list.
        z.append(x[i])

print("Challenge #2: Randomly generate two lists to test non-duplicated overlaps between lists")
print ("List X: ",x,"size:",int(size1))
print ("List Y: ",y,"size:",int(size2))
print ("Overlaps: ",sorted(z))          # If you want to use z.sort() here you have to do z.sort() on a given line by itself, and then print it. You can't do print(z.sort()).  (Why?)
