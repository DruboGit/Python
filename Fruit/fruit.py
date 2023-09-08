import random
import os

fruits = ("Apple", "Banana", "Pear", "Kiwi", "Cucumber", "Eggplant")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print(f"\nHere have a {fruits[fnr-1]}\n")

while looping:
    os.system("cls")
    i=0
    for fruit in fruits:
        print(f"{str(i+1)} : {fruit}")
        i += 1
    
    fruitnmr = input("\nWhich fruit would you like?: ")
    print_fruit(fruitnmr)
    
    
    quit = input ("Would you like to choose a fruit? y/n\n")
    if quit == "n":
        break