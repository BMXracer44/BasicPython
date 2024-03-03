#Alex Ferguson
#Python
#Mod 3 Assignment
#Due: 04/24/2023


stops = []
#Declares the list for all stops

def get_menu_option():
    print("\nVacation Planner: ")
    print("\t1. Add a stop")
    print("\t2. List all current stops")
    print("\t3. Clear all stops")
    print("\t4. End the program")
    return int( input("\tChoose an option: "))
#Function to display the menu and ask the user for input

def add_stop():
    stops.append(input("\nAdd a stop: "))
    return get_menu_option()
#Function to add a stop to the list and return the menu which returns the users option

def list_stops():
    print("\nStops: ")
    if len(stops) > 0:
        for stop in stops:
          print(f"\t{stop}")
    else:
        print("\tThere are no stops. ")
    return get_menu_option()
#Function to list all the stops in the stops list and return the menu which returns the users option

def clear_stops():
    stops = []
    print("\nStops have been cleared")
    return stops
#Function to clear all stops
#Returns the list "stops" as an empty list

user_input = get_menu_option()
#Starts asking for the users input so the while loop can run successfully 

while user_input != 4:
    if user_input == 1:
        user_input = add_stop()
    elif user_input == 2:
        user_input = list_stops()
    elif user_input == 3:
        stops = clear_stops()
        user_input = get_menu_option()
    else:
        print("Enter a valid number!")
        user_input = get_menu_option()
#While loop to keep the output running unless user would like to stop

print("Have a good vacation! ")
#Conclusion statement

