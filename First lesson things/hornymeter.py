hrony = input("On a scale of 1-10, how horny are you?\n")
if int(hrony) <= 3:
    print ("Good! :D")
elif int(hrony) > 3 and int(hrony) < 6:
    print ("Okay, close enough")
elif int(hrony) >= 6 and int(hrony) < 8:
    print ("Bad, go to corner and get less horny!")
elif int(hrony) >= 8 and int(hrony) <= 10:
    print ("BAD! Go to horny jail!")
elif int(hrony) > 10:
    print ("SUPER BAD! GO TO SUPER HORNY JAIL! I didn't even give you that option, you horny loner!")
input()