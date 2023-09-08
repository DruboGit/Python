import random
import os

coin = random.randint(1,2)
while True:
    os.system("cls")
    guess = input ("Heads or Tails?\n")
    if guess.lower() == "heads":
        g = 1
        guess = "Heads"
        break
    elif guess.lower() == "tails":
        g = 2
        guess = "Tails"
        break
    else:
        input ("Not a valid answer!")
if guess == "Heads":
    nguess = "Tails"
else:
    nguess = "Heads"
os.system("cls")
if g == coin:
    input (f"Congrats! It was indeed {guess}! :D\n")
else:
    input (f"Sorry it's wasn't {guess} it was {nguess} :(\n")