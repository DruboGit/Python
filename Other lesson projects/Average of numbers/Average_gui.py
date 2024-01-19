import tkinter as tk

root = tk.Tk()
root.title("Average")

def main():
    global entry
    tk.Label(text="Which numbers would you like to smooth out?").grid(sticky=tk.W, row=0, column=0)
    entry = tk.Entry(width=20)
    entry.grid(row=1, column=0)
    tk.Button(text="Enter", command=run).grid(row=2, column=0)
    root.mainloop()

def run():
    number = entry.get()
    split_number = number.split(" ")
    i=0
    finished = []
    finished.append(split_number[0])
    for num in split_number:
        if i != 0:
            if i != len(split_number)-1:
                new_num = str(round(((float(num)+float(split_number[i-1])+float(split_number[i+1]))/3),2))
                new_num = new_num.strip(".0")
                finished.append(str(new_num))
        i+=1
    finished.append(split_number[len(split_number)-1])
    output = " ".join(finished)
    tk.Label(text=f"Here is your finished product: {output}").grid(row=3, column=0)


main()