#!/usr/bin/python
#
# Practice Python Exercise #2
# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# 
# **  Ask the user for a number. Depending on whether the number is even or odd, 
#     print out an appropriate message to the user
#     Hint: how does an even / odd number react differently when divided by 2?
#
#  Extras:
#        ** If the number is a multiple of 4, print out a different message.
#        ** Ask the user for two numbers: one number to check (call it num) and
#           one number to divide by (check). If check divides evenly into num, tell 
#           that to the user. If not, print a different appropriate message.


print ("Python Exercise #2: Odd or Even?")
num = int(input("Enter a number to check:   "))

if num % 4 == 0:
    print("This number is even and divisible by 4!")
else:
    if num % 2 == 0:
      print("Even!")
    else:
      print("Odd!")

print ("Now we will ask for an input of two numbers.  A number to check, and a number to divide by.")
num = int(input("Enter a number to check:   "))
check = int(input("Enter number to divide by: "))
if num % check == 0:
    print("The number "+str(check)+" divides evenly into "+str(num)+"!  It does so "+str(int(num/check))+" times.")
else:
    print("The number "+str(check)+" does not divide evenly into "+str(num)+".  Sorry.")