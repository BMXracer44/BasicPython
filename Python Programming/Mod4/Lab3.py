#Alex Ferguson
#Python
#Mod 4 Lab 3
#04/25/2023

#Classes are named with UpperCamelCase
from helper import get_int

class GroceryItem:
    #Self refers to the current instance of the object
    def __init__(self, name, category, quantity):
        self.name = name
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}"
    
#I'm creating  a list and prepopulating it

groceries = [GroceryItem("Lettuce", "Produce", 2), 
             GroceryItem("Bread", "Bakery", 1),
             GroceryItem("Cereal", "Grain", 2),
             GroceryItem("Rice", "Grain", 3)
]

def get_menu_option():
    print("\n1. List Items")
    print("2. Update a quantity")
    print("3. Exit")
    return get_int("\tSelection: ")

def list_items():
    i = 1
    print()
    for item in groceries:
        print(f"{i}. {item.category} - {item.name}: {item.quantity}")
        i += 1

def update_quantity():
    list_items()
    item_index = get_int("\tWhich item would you life to modify: ")
    item = groceries[item_index - 1]
    item.quantity = get_int("\tNew Quantity: ")


user_input = get_menu_option()

while user_input != 3:
    if user_input == 1:
        list_items()
    elif user_input == 2:
        update_quantity()
    user_input = get_menu_option()   

print("Goodbye!")

