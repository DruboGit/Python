print("Input a number and it will return the next number with the same amount of 1s in binary")
number = input("Input: ")
b_number = "{0:b}".format(int(number))
ones = b_number.count("1")
i = int(number) + 1
while True:
    if ones != ("{0:b}".format(i)).count("1"):
        print(f"{i} = {'{0:b}'.format(i)} ({'{0:b}'.format(i).count('1')})")
        i += 1
    else:
        break
input(f"{i} = {'{0:b}'.format(i)} ({'{0:b}'.format(i).count('1')})")