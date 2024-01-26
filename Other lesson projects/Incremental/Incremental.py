import tkinter as tk
import time
import datetime as dt

root = tk.Tk()
root.title("Unnamed incremental")
money = 0
auto1 = 0
auto2 = 0
timer = 0
last_time = dt.datetime.timestamp(dt.datetime.now())
tickspeed = 1

def main():
    global au1
    global au1_butt
    global au2
    global au2_butt
    global moneys
    root.geometry("400x600")
    moneys = tk.Label(text=f"{money}$", font=(25))
    moneys.grid(row=0, column=0, sticky=tk.W)
    tk.Button(text="Add", command=money_button).grid(row=1, column=0, sticky=tk.W)
    au1 = tk.Label(text=f"Automatic 1 ({auto1}): ")
    au1.grid(row=2, column=0, sticky=tk.W)
    au1_butt = tk.Button(text="Buy:100$", command=automat1)
    au1_butt.grid(row=2, column=1, sticky=tk.W)
    au2 = tk.Label(text=f"Automatic 2 ({auto2}): ")
    au2.grid(row=3, column=0, sticky=tk.W)
    au2_butt = tk.Button(text="Buy:250$", command=automat2)
    au2_butt.grid(row=3, column=1, sticky=tk.W)
    while True:
        tick()
        root.update()

def automat1():
    global auto1
    global money
    auto1 += 1
    money -= 100
    
def automat2():
    global auto2
    global money
    auto2 += 1
    money -= 250

def money_button():
    global money
    money += 1
    moneys.config(text=f"{round(money)}$")

def tick():
    global money
    global timer
    global last_time
    global auto1
    au1.config(text=f"Automatic 1 ({auto1}): ")
    au2.config(text=f"Automatic 2 ({auto2}): ")
    current_time = dt.datetime.timestamp(dt.datetime.now())
    timer += current_time - last_time
    last_time = current_time
    moneys.config(text=f"{round(money)}$")
    if timer >= tickspeed:
        money += auto1
        auto1 += auto2
        timer = 0
    if money < 100:
        au1_butt.config(state="disabled")
    else:
        au1_butt.config(state="active")
    if money < 250:
        au2_butt.config(state="disabled")
    else:
        au2_butt.config(state="active")

main()