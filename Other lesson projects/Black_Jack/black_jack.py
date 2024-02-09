from deck import new_deck
from tkinter import *
import random as r
import time as t

deck = new_deck()
root = Tk()
root.title("Balck Jcak")
score1 = 0
score2 = 0

def main():
    global card_draw, score_b1, score_b2, hit, stand
    contain = Frame()
    contain.grid(row=0, column=0, padx=100, pady=25)
    Label (contain, text="Your score:").grid(row=0, column=0, sticky=N)
    Label (contain, text="Dealers score:").grid(row=0, column=1, sticky=N)
    score_b1 = Label(contain, text="00", font=("Arial", 50, "bold"))
    score_b2 = Label(contain, text="00", font=("Arial", 50, "bold"))
    score_b1.grid(row=1, column=0, sticky=N)
    score_b2.grid(row=1, column=1, sticky=N)
    hit = Button(contain, text="Hit", command=draw)
    stand = Button(contain, text="Stand", command=standy)
    hit.grid(row=2, column=0, sticky=N)
    stand.grid(row=2, column=1, sticky=N)
    card_draw = Label(contain, text="Cards bro")
    card_draw.grid(row=3, column=0, columnspan=2, sticky=N)
    root.mainloop()

def draw():
    global score1
    card = deck.pop(r.randint(0, len(deck)-1))
    card_draw.config(text=f"{card.type.name} of {card.suit.name}")
    if card.type.value == 1:
        if score1 <= 10:
            score1 += 11
        else:
            score1 +=1
    elif card.type.value > 10:
        score1 += 10
    else:
        score1 += card.type.value
    if score1 > 21:
        for widget in root.winfo_children():
            widget.destroy()
        Label(text="You Lose!", font=("Arial", 100, "bold")).grid(row=0, column=0, sticky=N)
        Label(text="You busted").grid(row=1, column=0, sticky=N)
    if score1 >= 10:
        score_b1.config(text=score1)
    else:
        score_b1.config(text=f"0{score1}")

def standy():
    global score2
    hit.config(state="disabled")
    stand.config(state="disabled")
    cnotine = True
    while cnotine == True:
        t.sleep(1)
        if score2 < score1:
            card = deck.pop(r.randint(0, len(deck)-1))
            card_draw.config(text=f"{card.type.name} of {card.suit.name}")
            if card.type.value == 1:
                if score2 <= 10:
                    score2 += 11
                else:
                    score2 +=1
            elif card.type.value > 10:
                score2 += 10
            else:
                score2 += card.type.value
            if score2 > 21:
                for widget in root.winfo_children():
                    widget.destroy()
                Label(text="You Win!", font=("Arial", 100, "bold")).grid(row=0, column=0, sticky=N)
                Label(text="Dealer busted").grid(row=1, column=0, sticky=N)
            if score2 >= 10:
                score_b2.config(text=score2)
            else:
                score_b2.config(text=f"0{score2}")
            root.update()
        else:
            if score1 == score2:
                if score1 == 20 or 21:
                    for widget in root.winfo_children():
                        widget.destroy()
                    Label(text="Tie!", font=("Arial", 100, "bold")).grid(row=0, column=0, sticky=N)
                else:
                    for widget in root.winfo_children():
                        widget.destroy()
                    Label(text="Dealer wins!", font=("Arial", 100, "bold")).grid(row=0, column=0, sticky=N)
                    Label(text="Tied below 20").grid(row=1, column=0, sticky=N)
            elif score2 > score1:
                for widget in root.winfo_children():
                    widget.destroy()
                Label(text="Dealer wins!", font=("Arial", 100, "bold")).grid(row=0, column=0, sticky=N)
                Label(text="Dealer stands at higher score").grid(row=1, column=0, sticky=N)
            cnotine = False

main()