import random as r
import os
import subprocess as s
dice = []
keep = []
finish = []
rollrule = 3

def main():
    global rollrule
    global keep
    global dice
    global finish
    while True:
        dietoroll = 5 - len(keep)
        dieroll(dietoroll)
        rollrule = rollrule - 1
        while True:
            cls()
            print (f"{dice}   Keep: {keep}   Rolls left: {rollrule}")
            cnotine = input("Would you like to lock any rolls?  y/n\n")
            if cnotine.lower() == "n":
                break
            lock = input("Which die would you like to lock in? A, B, C, D, E\n")
            lock = ord (lock.upper()) -65
            keep.append (dice.pop(lock))
        if rollrule <= 0:
            cls()
            finish = (dice + keep)
            cnotine = input (f"You have now rolled all your rolls   {finish}\nWould you like to roll again? y/n\n")
            if cnotine.lower() == "y":
                s.run(["python", "Yatzy.py"])
                int("balls")
            elif cnotine.lower() == "n":
                int("balls")



def dieroll(rolls):
    dice.clear()
    for i in range (rolls):
        roll = r.randint(1,6)
        dice.append (roll)
def cls():
    os.system("cls")

main()
