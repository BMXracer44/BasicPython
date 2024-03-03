#Alex Ferguson
#Python
#Mod 3 Lab 1
#04/18/23


#This is called a counter value or an indexing value
i = 0
while i < 5:
    print(i)
    # += is shorthand for i = i + 1
    i += 1


#Lets loop using user input
user_command = ''
while user_command != 'end':
    print("\nType \"end\" to exit the loop")
    user_command = input("\tCommand: ")

#This is how we create reuseable menus in programming
user_selection = 0
current_num = 0
while user_selection != 3:
    print(f"\nThe current number is: {current_num}")
    print("Select an option: ")
    print("\t(1) Add 1\n\t(2) Subtract 1\n\t(3) End the program")
    user_selection = int (input("\tSelect: "))
    
    if user_selection == 1:
        current_num += 1
    elif user_selection == 2:
        current_num -= 1

print("Isn't python so cool!?")