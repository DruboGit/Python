def main():
    number = input ("Which numbers would you like to smooth out?\n")
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
    input (f"Your finished product: {output}")

main()