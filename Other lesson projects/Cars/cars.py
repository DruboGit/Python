import car
import os

def main():
    global car
    while looping:
        cls()
        print("\n\t -:CarOutput:- ")

        i=0
        for car in carlist:
            print(f"{i+1} : {car.fabricator} : {car.color} : Amount= {car.storage}")
            i += 1

        car_num = input ("\nInput number for chosen car: ")
        car_num_int = int(car_num)

        storage_int = carlist[car_num_int-1].get_storage()
        storage_string = str(storage_int)

        if storage_int > 0:
            print(f"\nOne {carlist[car_num_int-1].color} {carlist[car_num_int-1].fabricator} coming up!")
            new_storage_int = storage_int - 1
            new_storage_str = int(new_storage_int)
            carlist[car_num_int-1].set_storage(new_storage_int)

        else:
            print("Sorry we do not have any more of those")

        print(f"Storage amount before: {storage_string}")
        print(f"Storage amount after: {new_storage_str}")        

        cnotine = input("\nWould you like to quit? y/n\n")
        if (cnotine == "y"):
            break



looping = True

volvo_black = car.Car("Volvo", "Black", 3)
fiat_white = car.Car("Fiat", "White", 10)
bugatti_pink = car.Car("Bugatti", "Pink", 1)

carlist = [volvo_black, fiat_white, bugatti_pink]

def cls():
    os.system("cls")
#print (f"Firt car = {carlist[0].fabricator}")

main()