#Alex Ferguson
#Python
#Mod 4 Lab 4
#04/25/2023

from helper import get_int

print("===Welcome to the Vehicle Manager===")

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
vehicles = [
    Vehicle("Toyota", "Highlander", 2004),
    Vehicle("Chevy", "Captiva Sport", 2012),
    Vehicle("Toyota", "Camry", 2005)
]

def get_menu_option():
    print("\n1. Add vehicle\n2. Remove vehicle\n3. Exit\n")
    return get_int("\tSelection: ")

def list_vehicles():
    i = 1
    print(f"\nYou have {len(vehicles)} vehicles: ")
    for vehicle in vehicles:
        print(f"{i}. {vehicle}")
        i += 1

def add_vehicle():
    vehicles.append(Vehicle(input("Enter make: "), input("Enter model: "), int(input("Enter year: "))))
    list_vehicles()

def remove_vehicle():
    list_vehicles()
    user_index = get_int("\n\tWhich vehicle would you like to remove: ") - 1
    vehicles.pop(user_index)
    if len(vehicles) > 0:
        list_vehicles()

user_input = get_menu_option()

while True:
    if user_input == 1:
        add_vehicle()
    elif user_input == 2:
        remove_vehicle()
    elif user_input == 3:
        break
    user_input = get_menu_option()

print("Goodbye!")