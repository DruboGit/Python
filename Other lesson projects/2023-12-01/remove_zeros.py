def main():
    print ("What number would you like to remove the unnecessary zero's from?")
    number = input ("Input: ")
    number = zero_remover(number)
    input (f"Output: {number}")

def zero_remover(number):
    number = float(number)
    if number.is_integer():
        return str(int(number))
    return str(number)

main()