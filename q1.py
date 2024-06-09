# make a class "Flower"
class Flower:
    # initialize each variable to an appropriate value
    def __init__(self,name = "flower",NumberOfPetals = 20,price = 35): 
        self.__name = name
        self.__NumberOfPetals = NumberOfPetals
        self.__price = price

    # methods for setting the value of each type
    def set_name(self,name = "flower"):
        self.__name = name
    def set_NumberOfPetals(self,NumberOfPetals = 20):
        self.__NumberOfPetals = NumberOfPetals
    def set_price(self,price = 35):
        self.__price = price

    # menthod of retrieving the value of each type
    def get_name(self):
        return self.__name
    def get_NumberOfPetals(self):
        return self.__NumberOfPetals
    def get_price(self):
        return self.__price

def main():
    while True:
        try:
            name=input("Please enter the name of the flower:")
            break
        except:
            print("Your input is invalid!")  # handle possible inappropriate inputs
            continue
    while True:
        try:
            NumberOfPetals=int(input("Please enter the number of petals:"))
            if NumberOfPetals <= 0:
                print("Please enter a posotive number!")
            else:
                break
        except:
            print("Your input is invalid!")  # handle possible inappropriate inputs
            continue
    while True:
        try:
            price=float(input("Please enter the price of the flower:"))
            if price <= 0:
                print("Please input a positive number!")
                continue
            else:
                break
        except:
            print("Your input is invalid!")  # handle possible inappropriate inputs
            continue
    my_flower = Flower(name,NumberOfPetals,price)
    print("The flower name is",my_flower.get_name())
    print("The number of petals is",my_flower.get_NumberOfPetals())
    print("The flower price is",my_flower.get_price())
main()