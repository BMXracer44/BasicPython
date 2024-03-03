#Alex Ferguson
#Python
#Mod 3 Lab 2
#04/18/23

import random

def random_number():
    minimum = int( input("Choose minimum number: "))
    maximum = int( input("Choose maximum number: "))
    return random.randint(minimum, maximum)

def guess_number():
    random_num = random_number()
    user_input = int( input("Guess a number: "))
    while user_input != random_num:
        if user_input > random_num:
            user_input = int ( input(f"{user_input} is too high! Guess again: "))
        elif user_input < random_num:
            user_input = int ( input(f"{user_input} is too low! Guess again: "))

    print(f"{user_input} is correct! ")

guess_number()
guess_number()
guess_number()