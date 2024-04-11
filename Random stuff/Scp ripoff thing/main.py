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
        mainpage()
    else:
        Label(text="Username and/or password incorrect",fg='red').place(x=50,y=125)

def mainpage():
    for i in root.winfo_children():
        i.destroy()
    root.geometry('350x100')
    Label(text=" ",pady=12).grid(row=0,column=0)
    Label(text=f"User: {username}").place(x=5,y=0)
    Label(text=f"Rank: Site Director").place(x=240,y=0)
    Label(text="Site Id: Site-1").place(x=240,y=15)
    new_entry = Button(text="New Entry",command=new_entry_fun)
    new_entry.grid(row=1,column=0)
    anomaly_list = Button(text="Anomaly List",command=a_list)
    anomaly_list.grid(row=1,column=1)
    site_inventory = Button(text="Site Inventory",state=DISABLED)
    site_inventory.grid(row=1,column=2)
    logs = Button(text="Logs",state=DISABLED)
    logs.grid(row=1,column=3)
    site_administration = Button(text="Administration", command=administration)
    site_administration.grid(row=1,column=4)

def new_entry_fun():
    root.geometry('250x100')
    for i in root.winfo_children():
        i.destroy()
    Button(text="Entity",command=e_entry, height=3, width=7).place(x=75,y=10)
    Button(text="Item", command=i_entry, height=3, width=7).place(x=135,y=10)
    Button(text="Back", command=mainpage).place(x=0,y=0)

def i_entry():
    i_ind = input("Item index: I-")
    file = open(f"Anomalies/I-{i_ind}.txt", 'a')
    file.write(f"Anomaly Index: I-{i_ind}\n\n")
    acl = input("Anomaly Containment Level: ")
    file.write(f"Anomaly Containment Level: {acl}\n\n")
    status = input("Status: ")
    file.write(f"Status: {status}\n\n")
    cp = input ("Containment Procedure: ")
    file.write(f"Containment Procedure: {cp}\n\n")
    desc = input("Description: ")
    file.write(f"Description: {desc}\n\n")
    doc = input("Documentation: ")
    file.write(f"Documentation: {doc}")
    file.close()
    mainpage()

def e_entry():
    e_ind = input("Entity index: E-")
    file = open(f"Anomalies/E-{e_ind}.txt", 'a')
    file.write(f"Anomaly Index: E-{e_ind}\n\n")
    acl = input("Anomaly Containment Level: ")
    file.write(f"Anomaly Containment Level: {acl}\n\n")
    status = input("Status: ")
    file.write(f"Status: {status}\n\n")
    cp = input ("Containment Procedure: ")
    file.write(f"Containment Procedure: {cp}\n\n")
    desc = input("Description: ")
    file.write(f"Description: {desc}\n\n")
    doc = input("Documentation: ")
    file.write(f"Documentation: {doc}")
    file.close()
    mainpage()

def a_list():
    pass

def administration():
    for i in root.winfo_children():
        i.destroy()
    Button(text="Back", command=mainpage).grid(row=0,column=0)
    Button(text="Site Id Change").grid(row=1,column=1)

def pdf(file):
    root.geometry('820x700')
    v = DocViewer(root)
    v.pack(side="top", expand=1, fill="both")
    v.display_file(file)

mainpage()

root.mainloop()
