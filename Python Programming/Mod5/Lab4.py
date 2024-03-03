#Alex Ferguson
#Mod 5 Lab 4
#Python
#5/2/2023

from helper import *

role_descrip = {
    "Administrator": "Duties relate to the functions of the college and supporting students outside of the classroom",
    "Instructor": "Support students through creation and execution of lesson plans",
    "Student": "Attend classes and complete coursework to earn a degree"
}

class Stakeholder:
    def __init__(self, firstname, lastname, email, role):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.role = role

    def __str__(self):
        return f"{self.lastname}, {self.firstname} | {self.role} | {self.email}\n\t{self.get_role_description()}"
    
    def get_role_description(self):
        if self.role in role_descrip:
            return role_descrip[self.role]
        else:
            return "No description"
        

stakeholders = [
    Stakeholder("Alex", "Ferguson", "fergusalex444@gmail.com", "Student")
]

def get_menu_option():
    print("\n1. List Stakeholders")
    print("2. Add a Stakeholder")
    print("3. List roles")
    print("4. Add a role")
    print("5. Exit")
    return get_int("\tSelection: ")

def list_stakeholders():
    for a in stakeholders:
        print(a)

def list_roles():
    for r, d in role_descrip.items():
        print(f"{r}:\n\t{d}")

def add_stakeholder():
    firstname = get_only_letters("Firstname: ")
    lastname = get_only_letters("Lastname: ")
    email = get_valid_email("Email: ")
    role = input("Role: ")
    new_stakeholder = Stakeholder(firstname, lastname, email, role)
    stakeholders.append(new_stakeholder)

def add_role():
    role = input("Role Title: ")
    description = input(f"{role} Description: ")
    role_descrip[role] = description

while True:
    option = get_menu_option()
    if option == 1:
        list_stakeholders()
    elif option == 2:
        add_stakeholder()
    elif option == 3:
        list_roles()
    elif option == 4:
        add_role()
    elif option == 5:
        break
    else:
        print("Enter valid option.")