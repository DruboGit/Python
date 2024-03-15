import os

cons = list("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")

def main():
    os.system("cls")
    output = ""
    conv = input("What would you like to convert?\n")
    for i in conv:
        if i in cons:
            output += (f"{i}o{i}")
        else:
            output += i
    input(output)
    main()

main()