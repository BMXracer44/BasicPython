#Alex Ferguson
#Python
#Mod 6 Lab 4
#05/09/2023
#OUR LAST LABBBBBBBBBBBBBBBBBB

import os
from helper import *

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.lastname}, {self.firstname}: Age -  {self.age}"
    
    def output_to_file(self, file_path):
        file = open(file_path, "a")
        file.write(self.__str__() + "\r")
        file.close()

people = [
    Person("Pushpa", "Aruna", 40),
    Person("Sandip", "Timeo", 80),
    Person("Trude", "Eudora", 16),
    Person("Berit", "Enyo", 25),
    Person("Aiolos", "Vibeke", 11),
    Person("Vegard", "Birgitr", 17),
    Person("Eirene", "Argus", 64),
    Person("Crius", "Midas", 32)
]

def get_menu_option():
    print("\n1. List files")
    print("2. Create file by age")
    print("3. Read file")
    print("4. Delete file")
    print("5. Exit")
    choice = get_int("\tSelection: ")
    return choice

def list_files():
    file_list = os.listdir("Lab4Files")
    print("Files in the Lab4Files folder: ")

    for file in file_list:
        print(file)

def create_file_by_age():
    file_name = input("Please enter file name: ")
    file_name = f"Lab4Files\{file_name}.txt"

    if os.path.exists(file_name):
        os.remove(file_name)

    min_age = get_int("Enter a minimum age: ")
    max_age = get_int("Enter a maximum age: ")

    for person in people:
        if person.age >= min_age and person.age <= max_age:
            person.output_to_file(file_name)

def read_file():
    wake_up = input("Name of file: ")
    if os.path.exists(f"Lab4Files\{wake_up}.txt"):
        file = open(f"Lab4Files\{wake_up}.txt", "r")
        print(file.read())
        file.close()
    else:
        print("That file does not exist")

def delete_file():
    the_last_function = input("File to delete: ")
    if os.path.exists(f"Lab4Files\{the_last_function}.txt"):
        os.remove(f"Lab4Files\{the_last_function}.txt")
    else:
        print("That file does not exist")

while True:
    choice = get_menu_option()
    if choice == 1:
        list_files()
    elif choice == 2:
        create_file_by_age()
    elif choice == 3:
        read_file()
    elif choice == 4:
        delete_file()
    elif choice == 5:
        break 


#if input in programs list, add (extra credit for assignment) 
#assignment is a little easier than the lab
