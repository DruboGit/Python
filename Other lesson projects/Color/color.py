import os
import sys

def main():
    os.system("cls")
    choice = input("Which way would you like to convert?:\nRGB to HEX (1)\nHEX to RGB (2) (WIP)\n")
    if choice == "1":
        rgb_to_hex()
    elif choice == "2":
        hex_to_rgb()
    else:
        input("That was not an option, try again")
        main()

def rgb_to_hex():
    os.system("cls")
    print("Format: RRR GGG BBB")
    value = input("RGB value: ")
    value = value.split(" ")
    if len(value) != 3:
        input("Only 3 sets of numbers accepted! Try again!")
        rgb_to_hex()
    for i in value:
        if int(i) > 255 or int(i) < 0:
            input(f"{i} is not inbetween 0 and 255")
            rgb_to_hex()
    new_val = []
    for i in value:
        new_val.append(hex(int(i)))
    for i in range(len(new_val)):
        new_val[i] = new_val[i].replace("0x", "")
    output = "".join(new_val)
    input(f"HEX value: #{output}")
    sys.exit()

def hex_to_rgb():
    os.system("cls")
    print("Format: HHHHHH")
    value = input("HEX value: ")


main()