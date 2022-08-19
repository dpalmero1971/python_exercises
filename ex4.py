#!/usr/bin/python
#
# Practice Python Exercise #4
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# 
# Create a program that asks the user for a number and then prints out a list of all the divisors 
# of that number. (If you don’t know what a divisor is, it is a number that divides evenly into 
# another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("Exercise #4: Divisors of a number")
print("Pring out a list of all the divisors of an entered value.")
i = int(input("Enter a number: "))
divisors=[]

# The exercise would like us to use a list for this, generated with range()...
# Supposedly generating a list of items this way is not as memory inefficient as it 
# sounds because internally python only "remembers" the beginning, end, and step 
# values of the range.

numbers=list(range(1,i+1))
for x in range(len(numbers)):         # or "for x in numbers:"
 if i % numbers[x] == 0:              #  if numbers % x == 0:
    divisors.append(x+1)
print(divisors)

# For loops require iterators, and iterators are lists, tuples, etc.
# It would seem to be more natural to do it with just integers, the "BASIC" way...
# But I guess the point is that Python and lists go together like Peanut Butter and Jelly.


divisors2=[]
iter = 1
while iter < i+1:
  if i % iter == 0:
    divisors2.append(iter)
  iter += 1
print(divisors2)        # The exercise still wants a list as output though.

# I suppose the while method is more clumsy, less elegant.

# The official solution:

listRange = list(range(1,i+1))
divisorList = []

for number in listRange:
    if i % number == 0:
        divisorList.append(number)
print(divisorList)

