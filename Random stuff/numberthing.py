from random import randint
import os
number = randint (1,10000000000)
attempts = 1
answer = input ("Guess a number between 1 and 10,000,000,000    Attempt:" + str(attempts) + "\n")
os.system("cls")
while True:
    if int(answer) == number:
        print("Congrats you have won! And it only took " + str(attempts) + " attempts!")
        input()
        break
    elif int(answer) != number and int(answer) < number:
        attempts = attempts + 1
        print("Not quite, higher    attempt:" + str(attempts) + "   last attempt:" + answer)
        answer = input ("Try again!\n")
        os.system("cls")
    elif int(answer) != number and int(answer) > number:
        attempts = attempts + 1
        print("Not quite, lower    attempt:" + str(attempts) + "    last attempt:" + answer)
        answer = input ("Try again!\n")
        os.system("cls")