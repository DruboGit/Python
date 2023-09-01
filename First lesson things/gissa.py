from random import randint
import os

number = randint (1,10)
answer = input ("Guess a number between 1 and 10\n")
os.system("cls")
if answer == number:
    print ("Woohoo! You got it right!")
if answer != number:
    print ("Wrong! You loose! It was actually " + str(number))
input()