from deck import new_deck
from tkinter import *
import random as r

deck = new_deck()
root = Tk()
root.title("Balck Jcak")
score1 = 0
score2 = 0

def main():
    global card_draw, score_b1
    contain = Frame()
    contain.grid(row=0, column=0, padx=100, pady=25)
    Label (contain, text="Your score:").grid(row=0, column=0, sticky=N)
    Label (contain, text="Dealers score:").grid(row=0, column=1, sticky=N)
    score_b1 = Label(contain, text="00", font=("Arial", 50, "bold"))
    score_b2 = Label(contain, text="00", font=("Arial", 50, "bold"))
    score_b1.grid(row=1, column=0, sticky=N)
    score_b2.grid(row=1, column=1, sticky=N)
    hit = Button(contain, text="Hit", command=draw)
    stand = Button(contain, text="Stand")
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
    elif card.type.value > 10:
        score1 += 10
    else:
        score1 += card.type.value
    if score1 >= 10:
        score_b1.config(text=score1)
    else:
        score_b1.config(text=f"0{score1}")

main()