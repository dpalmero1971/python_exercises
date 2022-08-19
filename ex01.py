#!/usr/bin/python
#
# Practice Python Exercise #1
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# 
# **  Create a program that asks the user to enter their name and their age. 
#     Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
#  Extras:
#        ** Add on to the previous program by asking the user for another number and printing out that 
#           many copies of the previous message. (Hint: order of operations exists in Python)
#        ** Print out that many copies of the previous message on separate lines. 
#           (Hint: the string "\n is the same as pressing the ENTER button)
#
currentyear=2021
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

msg = ("Hi,"+name+"! You will turn 100 years old in "+str(currentyear-age+100)+".")
print (msg)
i = int(input("How many times would you like me to repeat that message? "))

# Using just string manipulation
print (msg*i)           # No Carriage returns
print ((msg+"\n")*i)    # With Carriage returns and order of operations.


#Using a fancy for loop
#for x in range(i):
#    print(str(x+1)+":"+msg)


