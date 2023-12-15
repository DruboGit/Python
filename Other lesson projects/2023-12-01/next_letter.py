letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Å','Ä','Ö']

def main():
    change = input("Input: ")
    finish = changes(change)
    finish = (''.join(finish))
    input (f"Output: {finish}")

def changes(change):
    finish = []
    for i in range(len(change)):
        up = change[i].isupper()
        pain = (change[i]).upper()
        if pain == "Ö":
            next = 0
        elif pain == " ":
            finish.append(" ")
            continue
        else:
            next = letters.index(pain)+1
        new = letters[next]
        if not up:
            new = new.lower()
        finish.append(new)
    return finish

main()