import classes as c
import os
import sys
import random as r

player = None

def main():
    name = input("Enter your name: ")
    if name.strip().capitalize() == "Diezel":
        input("fuck off")
        sys.exit()
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")
    player = c.Trainer(name, gender, int(age), [], [])
    while True:
        os.system("cls")
        choice = input("Choose a Pokemon:\n1 - Bulbasaur\n2 - Pikachu\n3 - Lickitung\n4 - Mr. Mime\n5 - Magikarp\n6 - Ditto\n")
        ret = choose_pokemon(choice)
        if ret == False:
            continue
        player.party.append(ret)
        break
    input(f"You got {player.party[0].name}!")
    os.system("cls")
    opponent_age = r.randint(1, 100)
    if opponent_age >= 100:
        opponent_age = r.randint(100, 1000)
    opponent = c.Trainer(r.choice(c.random_names), r.choice(c.random_genders), opponent_age, [], [choose_pokemon(str(r.randint(1, 7)))])
    input(f"{opponent.name} the {opponent.age} year old {opponent.gender} wants to battle!\n{opponent.name} sent out {opponent.party[0].name}!\n")
    battle_hub(player.party[0], opponent.party[0])

def choose_pokemon(num):
    if num == "1":
        return c.Bulbasaur
    elif num == "2":
        return c.Pikachu
    elif num == "3":
        return c.Lickitung
    elif num == "4":
        return c.Mr_Mime
    elif num == "5":
        return c.Magikarp
    elif num == "6":
        return c.Ditto
    elif num == "7":
        return c.Mewtwo
    else:
        return False
    
def battle_hub(player : c.Pokemon, opponent : c.Pokemon):
    opp_health = opponent.stats.Health
    play_health = player.stats.Health
    while True:
        if play_health <= 0:
            input(f"{opponent.name} wins!")
            sys.exit()
        elif opp_health <= 0:
            input(f"{player.name} wins!")
            sys.exit()
        else:
            os.system("cls")
            print (f"{opponent.name} {opp_health}/{opponent.stats.Health} HP   VS   (You) {player.name} {play_health}/{player.stats.Health}")
            if (opponent.stats.Speed > player.stats.Speed) or (opponent.stats.Speed == player.stats.Speed and r.randint(1,2) == 1):
                input("Opponent is attacking")
                play_health -= round(calculate_damage(opponent.stats.Attack, player.stats.Defense, True if r.randint(1, 16) else False, 1))
                if play_health <= 0:
                    input(f"{opponent.name} wins!")
                    sys.exit()
                elif opp_health <= 0:
                    input(f"{player.name} wins!")
                    sys.exit()
                else:
                    os.system("cls")
                    print (f"{opponent.name} {opp_health}/{opponent.stats.Health} HP   VS   (You) {player.name} {play_health}/{player.stats.Health}")
                    choice = input ("What would you like to do?\nAttack (1)   \n")
                    if choice == "1":
                        opp_health -= round(calculate_damage(player.stats.Attack, opponent.stats.Defense, True if r.randint(1, 16) else False, 1))
            else:
                choice = input ("What would you like to do?\nAttack (1)   \n")
                if choice == "1":
                    opp_health -= round(calculate_damage(player.stats.Attack, opponent.stats.Defense, True if r.randint(1, 16) else False, 1))
                    play_health -= round(calculate_damage(opponent.stats.Attack, player.stats.Defense, True if r.randint(1, 16) else False, 1))

def calculate_damage(attack, defense, crit, effect_mult):
    power = 50
 
    return (((22 * power * attack / defense) / 50) * (2 if crit else 1) + 2) * effect_mult * (r.randint(217, 255) / 255)

main()