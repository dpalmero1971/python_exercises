#!/usr/bin/python
#
# Practice Python Exercise #9
# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# 
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess 
# the number, then tell them whether they guessed too low, too high, or exactly right. 
#
#  Extras:
#  ** Keep the game going until the user types “exit”
#  ** Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
playing=True
tries=0
a = random.randint(1,9)

print("Welcome to ex#9: Guessing Game!")
print("I'm thinking of a number between 1 and 9, inclusive.  Try to guess it!")
while playing == True:
  guess=input(str("Please guess a number between 1 and 9, or type exit to end game: "))
  guess=guess.lower()
  if guess == "exit":
    playing=False
    break
  if guess.isdigit() == False:
    print("Please guess a number between 1 and 9.")
    continue
  guess=int(guess)
  if guess < 1 or guess > 9:
    print("Please guess a number between 1 and 9.")
    continue
  if guess == a:
    print("You guessed correctly!")
    tries += 1
    print ("You guessed the number in",tries,"attempts.")
    continue
  elif guess > a:
    tries += 1
    print("You guessed too high!  Try a lower number.")
    continue
  elif guess < a:
    tries += 1
    print("You guessed too low!  Try a higher number.")
    continue