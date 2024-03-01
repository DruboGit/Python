import os
import sys

player_1_health = 3
player_2_health = 3

def main():
    while True:
        mode = input ("Which mode would you like to play?  10 (1) or 21 (2)(WIP)\n")
        if mode == "1":
            mode_10()
            break
        elif mode == "2":
            mode_21()
            break
        else:
            input ("Not a valid number, please try again")

def mode_10():
    global player_1_health, player_2_health
    num = 10
    while True:
        if num > 0:
            while True:
                os.system("cls")
                print (f"Player 1 turn   current number: {num}")
                choice = input ("Would you like to remove 1 or 2?\n")
                if choice == "1" or choice == "2":
                    num -= int(choice)
                    break
                else:
                    if player_1_health <= 0:
                        os.system("cls")
                        input("Player 2 wins!")
                        sys.exit()
                    else:
                        player_1_health -= 1
                        print("No! Thats NOT a valid number!")
                        input(f"You loose 1 life! You now only have {player_1_health}")
        elif num <= 0:
            os.system("cls")
            input ("Player 2 wins!")
            break
        if num > 0:
            while True:
                os.system("cls")
                print (f"Player 2 turn   current number: {num}")
                choice = input ("Would you like to remove 1 or 2?\n")
                if choice == "1" or choice =="2":
                    num -= int(choice)
                    break
                else:
                    if player_2_health <= 0:
                        os.system("cls")
                        input ("Player 1 wins!")
                        sys.exit()
                    else:
                        player_2_health -= 1
                        print("No! Thats NOT a valid number!")
                        input(f"You loose 1 life! You now only have {player_2_health}")
        elif num <= 0:
            os.system("cls")
            input ("Player 1 wins!")
            break


def mode_21():
    pass
main()