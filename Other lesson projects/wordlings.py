import os
import random as r
words = {}
num = 1

def main():
    global num
    while True:
        die()
        swedish = input("Please provide the Swedish word of choice: ")
        english = input("Please provide the English translation: ")
        words[swedish] = english
        num += 1
        cnotine = input (f"Add another word?   Yes(1)   No(2)    Words added: {num}\n")
        die()
        if cnotine == "2":
            break
    cnotine = None
    while True:
        swedish, english = r.choice(list(words.items()))
        words.pop(swedish)
        num -= 1
        while True:
            die()
            trans = input (f"What is this in english? {swedish}     Words left: {num}\n")
            if english.lower() == trans.lower():
                die()
                print("Congrats that is indeed correct!")
                if len (words) != 0:
                    cnotine = input("Would you like another word?   Yes(1)   No(2)\n")
                    if cnotine == "1":
                        break
                    elif cnotine == "2":
                        int("balls")
                else:
                    input ("Congrats you cleared the entire list!")
                    int("balls")
            elif trans != english:
                input("No try again!")

def die():
    os.system("cls")

main()
