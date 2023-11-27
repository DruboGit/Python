import os
import datetime as dt

today = dt.date.today()
year = list(str(today.year))
year.pop(0)
year.pop(0)
cur_year = str(f"{year[0]}{year[1]}")
sssn = ""

def main():
    while True:
        global sssn
        cls()
        print ("Be aware, this only checks Swedish Social Security Numbers in the format YYMMDDXXXX or YYYYMMDDXXXX!")
        sssn = list(input ("Which SSSN would you like to check? (must be numbers only or I will come to your house at 3am): \n"))
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
    if sssn2[8]%2 == 0:
        gender = "Female"
    else:
        gender = "Male"
    birth_y = (f"{sssn2[0]}{sssn2[1]}")
    if int(birth_y) > int(cur_year):
        birth_y = (f"19{birth_y}")
    else:
        birth_y = (f"20{birth_y}")
    birth_m = (f"{sssn2[2]}{sssn2[3]}")
    birth_d = (f"{sssn2[4]}{sssn2[5]}")
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
        input (f"\nThis SSSN is valid!\nGender: {gender}\nBirth Year: {birth_y}\nBirth Month: {birth_m}\nBirth Day: {birth_d}")
    else:
        input ("No. This SSSN is not valid!")

def cls():
    os.system("cls")

main()