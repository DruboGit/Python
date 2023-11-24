import os
sssn = ""

def main():
    while True:
        global sssn
        cls()
        print ("Be aware, this only checks Swedish Social Security Numbers in the format YYMMDDXXXX!")
        sssn = list(input ("Which SSSN would you like to check? (must be numbers or I will come to your house at 3am): \n"))
        if len(sssn) == 10:
            num10()
        elif len(sssn) == 12:
            num12()
        else:
            input ("This is not valid! (not 10 numbers)")
            continue

def num12():
    sssn.pop(0)
    sssn.pop(0)
    num10()

def num10():
    global sssn
    sssn2 = []
    last_num = int(sssn.pop(9))
    for i in sssn:
        sssn2.append(int(i))
    i = 0
    while i < 9:
        sssn2[i] *= 2
        i += 2
    sssn = []
    for i in sssn2:
        sssn.append(str(i))
    sssn = ''.join(sssn)
    sssn = list(sssn)
    sssn2 = []
    for i in sssn:
        sssn2.append(int(i))
    sum = 0
    for i in sssn2:
        sum += i
    check = (10-(sum%10))%10
    if check == last_num:
        input ("This SSSN is valid!")
    else:
        input ("No. This SSSN is not valid!")

def cls():
    os.system("cls")

main()