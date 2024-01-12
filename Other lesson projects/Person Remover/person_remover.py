import tkinter as tk

root = tk.Tk()
root.title("Person Remover Premium")
file = open("textfile.txt", encoding="utf-8-sig")
content = file.readlines()
people = []

def main():
    global entry
    i = 0
    for line in content:
        text = line
        adding(i, 0, text)
        i += 1
    for line in content:
        pers = line.split(":")
        per = pers[0]
        if per not in people:
            people.append(per)
        adding(0, 1, "Who would you like to remove?:")
        contain = tk.Frame(root)
        entry = tk.Entry(contain, width=20)
        entry.grid(row=1, column=1, sticky=tk.W)
        tk.Button(contain, text="Remove", command=remove).grid(row=1, column=2, sticky=tk.W)
        contain.grid(row=1, column=1, sticky=tk.W)
        i = 2
        for lines in people:
            adding (0, i, lines)
            i += 1
    root.mainloop()

def adding(row, column, text):
    add = tk.Label(root, text=text)
    add.grid(row=row, column=column, sticky=tk.W)

def remove():
    kill = entry.get()
    is_person = tk.Label(root, text="That is not a person")
    is_person.grid_remove()
    if kill not in people:
        is_person.grid(row=2, column=1, sticky=tk.W)
    else:
        i = 0
        for lines in content:
            per = lines.split(":")
            per = per[0]
            if per == kill:
                content.pop(i)
            i += 1
        new = open("Output.txt", "w")
        for line in content:
            new.write(line)
        is_person.grid_remove()
        tk.Label(root, text="Person has been removed!").grid(row=2, column=1, sticky=tk.W)

main()