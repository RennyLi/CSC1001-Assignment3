import random
from random import shuffle
from random import choice

class River:
    def __init__(self,length,fish_number,bear_number):  # initialize different values
        self.__length = length
        self.__contents = []

        # append fish, bear and None to the river list
        x = m = n = 0
        while x < fish_number:
            self.__contents.append("Fish")
            x += 1
        while m < bear_number:
            self.__contents.append("Bear")
            m += 1
        while n < (length - fish_number - bear_number):
            self.__contents.append(None)
            n += 1

        # randomize the elements of the river
        random.shuffle(self.__contents)
    
    def set_length(self,length):
        self.__length = length
    def set_fish_number(self,fish_number):
        self.__fish_number = fish_number
    def set_bear_number(self,bear_number):
        self.__bear_number = bear_number

    def simulation(self,i):
        none_index=[]
        for j in range(len(self.__contents)):
            if j == None:
                none_index.append(j)  # save the location of None element
        if i == 0:
            move = random.randint(0,1)
        if i == len(self.__contents) - 1:
            move = random.randint(-1,0)
        else:
            move = random.randint(-1,1)  # get a random move (left, right or stay still)
        if move != 0 and (0 <= i + move < self.__length - 1):
            # any animal can occupy a "None" location
            if self.__contents[i+move] == None:
                self.__contents[i+move] = self.__contents[i]
                self.__contents[i] = None
            
            # if two animals of same type collide, none of them disappear
            elif self.__contents[i+move] == self.__contents[i]:
                self.__contents[i] = self.__contents[i]
                self.__contents[i+move] = self.__contents[i+move]
                # create a new instance of the type and place in a random empty
                if none_index != []:
                    random_location = choice(none_index)
                    self.__contents[random_location] = self.__contents[i]

            # Bear collide the fish, bear occupies fish's location and fish disappears
            elif self.__contents[i+move] != self.__contents[i] and self.__contents[i] == "Bear":
                self.__contents[i] = None
                self.__contents[i+move] = "Bear" 

            # fish collides the bear, bear doesn't change, fish disappears
            else:
                self.__contents[i] = None
                self.__contents[i+move] = self.__contents[i+move]
    
    def update_river(self):
        # save the animal location
        animal_index=[]
        for i in range(len(self.__contents)):
            if self.__contents[i] != None:
                animal_index.append(i)
        
        # in each simulation, the animal take actions one by one
        for i in animal_index:
            self.simulation(i)

    def print_river(self):  # print the result
        result =""
        for x in self.__contents:
            if x == "Bear":
                result += "B"
            elif x == "Fish":
                result += "F"
            else:
                result += "N"
        print(result)

def main():
    length = int(input("Please enter the initial value of the river length:"))
    fish_number = int(input("Please enter the number of fishes:"))
    bear_number = int(input("Please enter the number of bears:"))
    river = River(length,fish_number,bear_number)  # create an instance
    random_moving_step = int(input("Please enter the number of steps of the random moving process:"))
    t = 0
    while t < random_moving_step:  
        river.print_river()
        river.update_river()
        t += 1

main()
