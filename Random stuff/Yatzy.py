import random as r
import os
dice = []
keep = []

def main():
    dietoroll = 5 
    while True:
        dieroll(dietoroll)
        print (dice)
        while True:
            cnotine = input("Would you like to lock any rolls?  y/n\n")
            if cnotine.lower() == "n":
                break
            lock = input("Which die would you like to lock in? A, B, C, D, E\n")
            lock = ord (lock.upper()) -65
            keep.append (dice.pop(lock))
            



def dieroll(rolls):
    dice.clear()
    for i in range (rolls):
        roll = r.randint(1,6)
        dice.append (roll)

main()