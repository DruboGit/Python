import sqlite3
import os
import random as r

sqlconnect = None
cursor = None
prizes = [
    "One aglet",
    "Cat ears (stolen from Nils)",
    "One snowball (incoming at 299 792 458 m/s)",
    "Half a skateboard",
    "A double A battery",
    "Crusty sock",
    "Ticket for 9/11 recreation"
]

def p_start():
    while True:
        cls()
        print ("What would you like to do?\n")
        cnotine = input ("\nEdit lists      (1)\nEdit words      (2)\nPractice words  (3)\n")
        if cnotine == "1":
            edit_list()
        elif cnotine == "2":
            edit_words()
        elif cnotine == "3":
            practice()
        else:
            cls()
            input ("\nNo! Input a valid number!")
            p_start()

def edit_list():
    sql()
    while True:
        cls()
        cnotine = input("Add new list  (1)\nRemove existing list  (2)\nGo back  (3)\n")
        if cnotine == "1":
            cls()
            name = input ("What would you like it to be called?\n")
            create_table = f"""CREATE TABLE IF NOT EXISTS {name} (
                            id INTEGER PRIMARY KEY,
                            word TEXT NOT NULL,
                            translation TEXT NOT NULL
                            )"""
            cursor.execute(create_table)
        elif cnotine == "2":
            cls()
            cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
            for table in cursor:
                print (table[0])
            remove = input("Which one would you like to remove?\n")
            cursor.execute(f"DROP TABLE {remove}")
        elif cnotine == "3":
            cursor.close()
            sqlconnect.close()
            break
def edit_words():
    sql()
    active = True
    while active == True:
        cls()
        print ("Which list would you like to edit?\n")
        cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        for table in cursor:
            print (table[0])
        select = input ()
        while True:
            cls()
            cnotine = input ("Add new words  (1)\nRemove words   (2)\nGo back        (3)\n")
            if cnotine == "1":
                cls()
                w = input ("Word: ")
                wt = input ("Translation: ")
                insert = f"""INSERT INTO {select}
                             (word,translation)
                             VALUES
                             ('{w}','{wt}')"""
                cursor.execute(insert)
                sqlconnect.commit()
            elif cnotine == "2":
                cls()
                print ("What word would you like to remove?\n")
                cursor.execute(f"SELECT * from {select} ORDER by id")
                words = cursor.fetchall()
                for row in words:
                    print (f"{row[0]}.  Word: {row[1]}  Translation: {row[2]}")
                remove = input()
                cursor.execute(f"DELETE FROM {select} WHERE id = {remove}")
                increment = f"""CREATE TABLE new_table (
                                id INTEGER PRIMARY KEY,
                                word TEXT NOT NULL,
                                translation TEXT NOT NULL)
                            """

                increment2 = f"""INSERT INTO new_table (word, translation)
                            SELECT word, translation FROM {select};"""
                cursor.execute(increment)
                cursor.execute(increment2)
                cursor.execute(f"DROP TABLE {select}")
                cursor.execute(f"ALTER TABLE new_table RENAME TO {select}")
                sqlconnect.commit()
            elif cnotine == "3":
                cursor.close()
                sqlconnect.close()
                active = False
                break
def practice():
    cls()
    sql()
    print ("Which list would you like to practice?\n")
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    for table in cursor:
        print (table[0])
    select = input ()
    cursor.execute(f"SELECT COUNT(id) FROM {select}")
    amount = int(cursor.fetchone()[0])
    if amount == 0:
        input ("Sorry this list does not have any words. Please try with another list")
    else:
        words = {}
        num = 0
        cursor.execute(f"SELECT * from {select} ORDER by id")
        temp = cursor.fetchall()
        for row in temp:
            word = row[1]
            trans = row[2]
            print(row[1])
            words[word] = trans
            num += 1
        while True:
            cls()
            if len(words) == 0:
                input(f"Yay! You have cleared your list of words! Here is a prize: {r.choice(prizes)}")
                break
            else:
                word, trans = r.choice(list(words.items()))
                while True:
                    cls()
                    guess = input (f"Please translate this word:  {word}    Words left: {num}\n")
                    if trans.lower() == guess.lower():
                        cls()
                        input (f"Yippe! You got it right!             Words left: {num}\n")
                        words.pop(word)
                        num -= 1
                        break
                    else:
                        input("Nope! Try again!")

        
def cls():
    os.system("cls")

def sql():
    global sqlconnect, cursor
    sqlconnect = sqlite3.connect("word.db")
    cursor = sqlconnect.cursor()
    

p_start()