import requests
import os
import time

web = 'http://10.155.16.115:5000'
#r = requests.get(web)
#data = requests.post(web, 'Hello')
while True:
    s_or_r = input ("Would you like to send or receive a message?\n")
    if s_or_r == "send":
        while True:
            message = input("What would you like to send?\n")
            requests.post(web, message)
            os.system("cls")
    elif s_or_r == "receive":
        while True:
            r = requests.get(web)
            os.system("cls")
            print (r.text)
            time.sleep(2)
    else:
        input("No, try again")
        os.system("cls")