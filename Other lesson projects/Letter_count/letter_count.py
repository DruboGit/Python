import os

counted = []

def main():
    os.system("cls")
    x = input ("What would you like to count?:\n")
    x = x.upper()
    x = x.replace(" ","")
    for i in x:
        if x.count(i) != 0:
            counted.append(f"{i}: {x.count(i)}")
        x = x.replace(i,"")
    counted.sort()
    for i in counted:
        print(i)
    input()
        

main()