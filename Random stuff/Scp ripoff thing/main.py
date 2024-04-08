from tkinter import *
from tkdocviewer import *

root = Tk()
username = "Ballman"

def login():
    root.geometry('300x150')
    Label(text="Username:").place(x=20,y=10)
    user = Entry()
    user.place(x=100,y=10)
    Label(text="Password:").place(x=20,y=40)
    password = Entry(show="*")
    password.place(x=100,y=40)
    enter = Button(text="Login",command=lambda:validate(user.get(),password.get()))
    enter.place(x=120,y=70)
    create_account = Button(text="Create account", state=DISABLED)
    create_account.place(x=95,y=97)

def validate(user,password):
    if user == username and password == "2996":
        for i in root.winfo_children():
            i.destroy()
        mainpage()
    else:
        Label(text="Username and/or password incorrect",fg='red').place(x=50,y=125)

def mainpage():
    root.geometry('350x100')
    Label(text=" ",pady=3).grid(row=0,column=0)
    Label(text=f"User: {username}").place(x=5,y=0)
    Label(text=f"Rank: Site Director").place(x=240,y=0)
    new_entry = Button(text="New Entry",command=new_entry ,state=DISABLED)
    new_entry.grid(row=1,column=0)
    creature_list = Button(text="Creature List",state=DISABLED)
    creature_list.grid(row=1,column=1)
    site_inventory = Button(text="Site Inventory",state=DISABLED)
    site_inventory.grid(row=1,column=2)
    logs = Button(text="Logs",state=DISABLED)
    logs.grid(row=1,column=3)
    site_administration = Button(text="Administration",state=DISABLED)
    site_administration.grid(row=1,column=4)

def new_entry():
    

def pdf(file):
    root.geometry('820x700')
    v = DocViewer(root)
    v.pack(side="top", expand=1, fill="both")
    v.display_file(file)

login()

root.mainloop()
