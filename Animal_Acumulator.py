

#import the random module
import random

CON = 42
# This displays the instrution for the game
def instrctions():
    print("Welcome to the Animal Accmulator\nAnimals cost and generate income according to their name length(e.g aZebra costs 5)\nEach day, animals generate income your animals generates.\nWould you like to load your animals from animals.txt(Y/n)? n\nYou start with these animals:\nExample:\nAntelope, Fox, Zebra,\nAfter 0 days, you have 3 animals and your income is 0.")


# We create a funtion that takes the user input
def choose():
    user_input = ''
    while True:
        user_input = input(
            '(W)ait\n(D)isplay animals\n(A)dd animal\n(Q)uit\nChoose:')
        user_input.lower()
        if user_input == 'w':
            luck =  random.randint(0,100)
            animals= nimals()
            inco = income()
            days =  day()
            to_in = total_income()
            # this cheaks the luck to kno if it is greater or equal to the con
            if luck < 42:
                animal_escape = random.choice(animals)
                animals.remove(animal_escape)
                print(f"{animal_escape} has escaped! ")

            inco = 0
            for animal in animals:
                inco+=(luck // 100 * len(animals))
            days +=1
            to_in += inco
            

            print(f"Today's lucky number is {luck}.")
            print(f"After {days} days, you have {len(animals)} animals and your total income {to_in}.")
            print(inco)

        elif user_input == 'a':
            animal = nimals()
            to = total_income()
            add_animals(animal)
    

        elif user_input == 'd':
            animals = nimals()
            display(animals)
            
        elif user_input == 'q':
            break
        else:
            print('invaild choice ')
            
# This is for the funtion keeping the animal 
def nimals():
    animals = ["Antelope, Fox, Zebra"]
    return animals

# This is the function that calculate the income of the user
def income():
    income = 0
    return income

# this is funtion generated random number as luck
def luck():
    lucks =  random.randint(0,100)
    return lucks
    

# this the profit made by the user
def gain():
    gains = 0
    return gains

# this is the function for the length of the animals
def length_of_animals():
    an = nimals()
    length_of_animal = len(an)
    return length_of_animal

# This is for the losses the user gets
def loss():
    lost = 0
    return lost

# this is the function for list of animals
def number_of_each_animals():
    animal = nimals()
    for i in animal:
        lenght = len(i)
    return lenght

# this function keeps record of the days
def day():
    day = 0
    return day


# this is the funtion that keeps record of the animals lost
def lost_animals():
    lost = "None"
    return lost

# this funtion is to adding and buying a new funtion
def add_animals(animals):
    animal = input("Animal name: ").title()
    if animal in animals:
        print(f"The animal {animal} already in the list")
    else:
        animals.append(animal)
        print("Animal added")

    
# this cheacks the balance of the user
def total_income():
    inc = income()
    gan = gain()
    bal = inc + gan
    return bal

#def Wait():
    luck = luck()

    

def display(animals):
    for animal in animals:
        if animal == " ":
            print("No animals")
        else:
            pass
        print("-" ,animal)

    


def main_menu():
    instrction = instrctions()
    while True:
        user_choice = choose()
    
    
    

main_menu()
