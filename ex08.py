#!/usr/bin/python
#
# Practice Python Exercise #8
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# 
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of 
# congratulations to the winner, and ask if the players want to start a new game)
# 
# Concepts for this exercise:  While, Infinite, Break

# Below solution is somewhat lengthy -- other people had some clever solutions with using +1 mod % 3 to calculate winner


stillplaying=True
rps=['Rock','Paper','Scissors']
yesno=["Y","N"]
p1=""
p2=""
again=""

print("Welcome to our silly Rock-Paper-Scissors game!")
while stillplaying == True:
    while p1 not in rps:
        p1=input(str("Player 1:  Its your move: type Rock, Paper, or Scissors: "))
        p1=p1.capitalize()
    while p2 not in rps:
        p2=input(str("Player 2:  Its your move: type Rock, Paper, or Scissors: "))
        p2=p2.capitalize()
    if p1 == p2:
        print ("The game is a tie!")
    elif p1 == "Rock":
      if p2 == "Scissors":
          print("Player 1 wins!  Rock > Scissors.")
      else:
          print("Player 2 wins!  Paper > Rock.")
    elif p1 == "Paper":
        if p2 == "Rock":
          print("Player 1 wins!  Paper > Rock.")
        else:
          print("Player 2 wins!  Scissors > Paper.")
    elif p1 == "Scissors":
        if p2 == "Paper":
          print("Player 1 wins!  Scissors > Paper.")
        else:
          print("Player 2 wins!  Rock > Paper.")
    while again not in yesno:
      again = input(str("Would you like to play again?  Y/N: "))
      again=again.capitalize()
    
    if again == "Y":
        stillplaying == True
        p1=""
        p2=""
        again=""
    else:
        stillplaying == False
        break





