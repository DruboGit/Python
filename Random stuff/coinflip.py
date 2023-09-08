import random
import os

coin = random.randint(1,2)
while True:
    os.system("cls")
    guess = input ("Heads or Tails?\n")
    if guess == str("Heads"):
        g = 1
        break
    elif guess == str("Tails"):
        g = 2
        break
    else:
        input ("Not a valid answer!")
if guess == str("Heads"):
    nguess = "Tails"
else:
    nguess = "Heads"
os.system("cls")
if g == coin:
    input (f"Congrats! It was indeed {guess}! :D\n")
else:
    input (f"Sorry it's wasn't {guess} it was {nguess} :(\n")