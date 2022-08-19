#!/usr/bin/python
#
# Practice Python Exercise #10
# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# 
#  Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = []
#
# and write a program that returns a list that contains only the elements that are common between the 
# lists (without duplicates). Make sure your program works on two lists of different sizes. Write this
# using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
# 
#
# Extra:
# ** Randomly generate two lists to test this
# ** Write in one line of python using sets ( - but sets have not yet been discussed )
#
print ("Welcome to exercise 10: List Overlap comprehensions.")
print ("First iteration is with predefined lists called 'a' and 'b', where b is the longer list:")

# Create a list of all overlaps, including duplicates, in one line
c = [a[i] for i in range(len(a)) if a[i] in b]

for i in range(0,len(c)):                           #remove duplicates
  if c[i] not in d:
    d.append(c[i])

print(d)

# Extra Credit
import random
print("The second iteration is with two lists of random size containining random numbers between 1 and 50:")

size1=0
size2=0
w = []
x = []
y = []
z = []

size1=random.randint(10,30)                         # The first list will be size1 in length
size2=random.randint(size1+1,35)                    # The second list will be size2 in length, which will always be > than size1

w=sorted(random.sample(range(50),size1))            # Generate size1 amount of random numbers between 1 and 50 and assign to list w
x=sorted(random.sample(range(50),size2))            # Generate size2 amount of random numbers between 1 and 50 and assign to list x

y = [w[i] for i in range(len(w)) if w[i] in x]      # Generate a list of overlaps and assign to list y

for i in range(0,len(y)):                           # Write all non-duplicates from list y to list z.
  if y[i] not in z:
    z.append(y[i])
    z.sort()

print ("List 1:",w)
print ("List 2:",x)
print ("Overlaps:",z)