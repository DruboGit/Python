import sqlite3
import os
import random as r
import tkinter as tk

root = tk.Tk()
root.title("Wordlings v3")


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
    cls()
    root.geometry("210x50")
    do = tk.Label(root, text="What would you like to do?")
    do.grid(row=0, column=0, sticky=tk.N)
    butt_contain = tk.Frame(root)
    butt_contain.grid(row=1, column=0)
    list = tk.Button(butt_contain, text="Edit lists", command=edit_list)
    list.grid(row=0, column=0, sticky=tk.W)
    words = tk.Button(butt_contain, text="Edit words", command=edit_words)
    words.grid(row=0, column=1, sticky=tk.W)
    pract = tk.Button(butt_contain, text="Practice words", command=practice)
    pract.grid(row=0, column=2, sticky=tk.W)

def edit_list():
    cls()
    sql()
    root.geometry("500x500")
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    labels = []
    tk.Button(text="Back", command=p_start).grid(row=0, column=0, sticky=tk.W)
    tk.Button(text="Add new list", command=add_list).grid(row=99, column=0, sticky=tk.W)
    num = 0
    for i in cursor:
        labels.append(tk.Label(text=f"{i[0]}"))
        kill = i
        tk.Button(text="Remove", command=lambda: drop_child(kill)).grid(row=num+1, column=1, sticky=tk.W)
        num += 1
    for i in range(len(labels)):
        labels[i].grid(row=i+1,column=0, sticky=tk.W)

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
def drop_child(table):
    cursor.execute(f"DROP TABLE {table[0]}")
    edit_list()

def add_list():
        global enter
        enter = tk.Entry(root, width=25)
        enter.grid(row=100, column=0, sticky=tk.W)
        tk.Button(text="Add", command=lambda: new_list()).grid(row=100, column=1)
        tk.Button(text="Cancel", command=edit_list).grid(row=100, column=2)

def new_list():
    list_name = enter.get()
    create_table = f"""CREATE TABLE IF NOT EXISTS {list_name} (
                    id INTEGER PRIMARY KEY,
                    word TEXT NOT NULL,
                    translation TEXT NOT NULL
                    )"""
    cursor.execute(create_table)
    edit_list()

def cls():
    for i in root.winfo_children():
        i.destroy()

def sql():
    global sqlconnect, cursor
    sqlconnect = sqlite3.connect("word.db")
    cursor = sqlconnect.cursor()
    

p_start()
root.mainloop()