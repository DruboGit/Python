import os
import sqlite3
def main():
    while True:
        add_dog()
        list_dogs()
        answer = input("\nWould you like to add a dog? y/n")
        if answer !="y":
            break

def add_dog():
    os.system("cls")
    dogname = input ("\nPlease eneter dogs name: ")
    dograce = input ("\nPlease enter dog race: ")

    sqliteconnection = sqlite3.connect("dogs.db")
    cursor = sqliteconnection.cursor()
    sqlite_insert = f"""INSERT INTO dogs
                        (name,race)
                        VALUES
                        ('{dogname}','{dograce}')"""
    
    cursor.execute(sqlite_insert)
    sqliteconnection.commit()
    print ("\nAdded dog to database\n")
    cursor.close()
    sqliteconnection.close()

def list_dogs():
    sqliteconnection = sqlite3.connect("dogs.db")
    cursor = sqliteconnection.cursor()
    sqlite_select = """SELECT * from dogs ORDER by name"""
    cursor.execute(sqlite_select)
    records = cursor.fetchall()
    for row in records:
        print (f"\tID: {row[0]}, \tNAME: {row[1]} \tRACE: {row[2]}")
    cursor.close()
    sqliteconnection.close()
    print("Connection has been closed. Bye Bye!")

main()