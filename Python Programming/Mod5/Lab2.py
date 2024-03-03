#Alex Ferguson
#Mod 5 Lab 2
#Python
#5/2/2023

from helper import get_int

#wE CAN STORE LISTS INSIDE OF A DICTIONARY
flag_colors = {
    "Canada": ["red", "white"],
    "United States": ["red", "white", "blue"],
    "Mexico": ["red","white", "green"]
}

def list_flags():
    for key, value in flag_colors.items():
        print(f"\n{key}")


        formatted_colors = ', '.join(value)
        print(f"\t{formatted_colors}")

def add_flag():
    country_name = input("\nEnter the name of a country: ")
    colors = []
    while True:
        color = input("\tEnter a color (type \"!\" to end): ")
        if color == "!":
            #sentinal values are used to exit a loop
            break
        else:
            colors.append(color)

    #Adds or updates the value for the key
    flag_colors[country_name] = colors

def get_colors_by_name(key):
    if key in flag_colors:
        print(", ".join(flag_colors[key]))
    else:
        print("That is not in the list")

while True:
    print("\n1. List Flags")
    print("2. Add Flag")
    print("3. Get flag colors by country")
    print("4. Exit")
    choice = get_int("\tSelection: ")
    if choice == 1:
        list_flags()
    elif choice == 2:
        add_flag()
    elif choice == 3:
        get_colors_by_name(input("\nEnter the name of a country: "))
    else:
        break

print("\nThanks for using the flag colors program!")
