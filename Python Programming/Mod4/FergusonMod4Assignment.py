#Alex Ferguson
#Python
#Assignment
#04/25/2023

from helper import get_int_in_range


print("===Gym Lift Tracker===")

class Lift:
    def __init__(self, name, muscleGroup, weight):
        self.name = name
        self.muscleGroup = muscleGroup
        self.weight = weight

    def __str__(self):
        return f"Name: {self.name}\nMuscle group: {self.muscleGroup}\nWeight: {self.weight}"

lifts = [
    Lift("Squat", "Legs", 305),
    Lift("Bench", "Arms", 225)
]

def get_menu_options():
    print("\n1. Add life\n2. Remove lift\n3. Update weight\n4. Exit")
    return get_int_in_range("\tSelection: ", 1, 4)

def list_lifts():
    i = 1
    for lift in lifts: 
        print(f"\n{i}. {lift}")
        i += 1

def add_lift():
    list_lifts()
    lifts.append(Lift(input("\nInput new lift: "), input("Input muscle group: "), int(input("Input weight: "))))
    list_lifts()

def remove_lift():
    if(len(lifts) > 0):
        list_lifts()
        user_index = get_int_in_range("\tWhich lift would you like to remove: ", 1, len(lifts))
        lifts.pop(user_index - 1)
        list_lifts()
    else:
        print("There are no lifts to remove! ")

def update_lift_weight():
    list_lifts()
    user_index = get_int_in_range("\n\tWhich lift would you like to update: ", 1, len(lifts))
    lifts[user_index - 1].weight = int(input("Input new weight: "))
    list_lifts()

user_input = get_menu_options()

while user_input != 4:
    if user_input == 1:
        add_lift()
    elif user_input == 2:
        remove_lift()
    elif user_input == 3:
        update_lift_weight()

    user_input = get_menu_options()

print("Thank you for using the Gym Lift Tracker!")

