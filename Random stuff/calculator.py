import os
def addition (num1, num2):
    return int(num1) + int(num2)
def subtraction (num1, num2):
    return int(num1) - int(num2)
def divition (num1, num2):
    return int(num1) / int(num2)
def multiplication (num1, num2):
    return int(num1) * int(num2)

quit = 2
while True:
    if int(quit) == 1:
        break
    elif int(quit) == 2:
        os.system("cls")
        math = input ("(1)Addition  (2)Subtraction  (3)Divition  (4)Multiplication\n")
        if int(math) == 1:
            os.system("cls")
            number1 = input ("First number:")
            os.system("cls")
            number2 = input ("First number: " + number1 + "\nSecond number:")
            os.system("cls")
            answer = addition (number1, number2)
            print ("First number: " + number1 + "\nSecond number: " + number2 + "\nAnswer: " + str(answer))
            exit = input ("\n(1)Go back  (2)Exit\n")
            if exit == 1:
                quit = 2
                break
            elif exit == 2:
                math = None
                quit = 1
                continue
        elif int(math) == 2:
            os.system("cls")
            number1 = input ("First number:")
            os.system("cls")
            number2 = input ("First number: " + number1 + "\nSecond number:")
            os.system("cls")
            answer = subtraction (number1, number2)
            print ("First number: " + number1 + "\nSecond number: " + number2 + "\nAnswer: " + str(answer))
            exit = input ("\n(1)Go back  (2)Exit\n")
            if exit == 1:
                continue
            elif exit == 2:
                exit = "exit"
                print (int(exit))
        elif int(math) == 3:
            os.system("cls")
            number1 = input ("First number:")
            os.system("cls")
            number2 = input ("First number: " + number1 + "\nSecond number:")
            os.system("cls")
            answer = divition (number1, number2)
            print ("First number: " + number1 + "\nSecond number: " + number2 + "\nAnswer: " + str(answer))
            exit = input ("\n(1)Go back  (2)Exit\n")
            if exit == 1:
                continue
            elif exit == 2:
                exit = "exit"
                print (int(exit))