import lottery
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Lottery")
root.geometry("380x300")

label_amount = tk.Label(root, text="Amount of lots:")
label_amount.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

textbox_amount = tk.Entry(root, width=2)
textbox_amount.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
textbox_amount.focus_set()

def update_listbox(amount_lots):
    listbox.delete(0, tk.END)
    listbox.insert(1, "You win! This is your prize: ")

    try:
        int_amount = int(amount_lots)
        i=0
        if(int_amount <= 3):
            while i < int_amount:
                winning = lottery.get_prize()
                listbox.insert((i+2), winning)
                i = i+1
        else:
            messagebox.showinfo("No")
    except:
        messagebox.showinfo("No")

def click_button():
    amount_lot = textbox_amount.get()
    textbox_amount.delete(0, tk.END)
    update_listbox(amount_lot)

button_sub = tk.Button(text="Try your luck!", command=click_button)
button_sub.grid(row=1, column=0, sticky=tk.E, padx=15, pady=13)

listbox = tk.Listbox(root, height=4, width=30, bg="White", activestyle="dotbox", font="Helvetica", fg="black")
listbox.grid(row=2, column=0, columnspan=2, padx=14, pady=15)

root.mainloop()
