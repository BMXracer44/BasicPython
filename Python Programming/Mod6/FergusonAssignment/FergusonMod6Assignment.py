#Alex ferguson
#Python
#Mod 6 Assignment (final assignment)
#05/09/2023

from helper import *
import os

print("======Final Assignment======")
#Introduction statement

class Student:
    def __init__(self, firstname, lastname, username, semester, program):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.semester = semester
        self.program = program

    def __str__(self):
        return f"{self.lastname}, {self.firstname} | {self.program} - Semester {self.semester}"
    
    def output_to_file(self, file_path):
        file = open(file_path, "a")
        file.write(self.__str__() + "\r")
        file.close()
#Creates student

students = [
    Student("Pushpa", "Aruna", "pushpa14", 3, "Web and Software"),
    Student("Sandip", "Timeo", "sandip12", 2, "Cybersecurity"),
    Student("Trude", "Eudora", "trudee25", 1, "Network Specialist"),
    Student("Berit", "Enyo", "beritt62", 4, "Cybersecurity"),
]
#Initializes the students in a list of students


def add_student():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = get_username("Username: ")
    semester = get_int("Semester: ")
    program = get_program("Program: ")

    students.append(Student(first_name, last_name, username, semester, program))
#Adds student to the list of students


def create_file():
    file_name = input("Report Name: ")
    file_name = f"AssignmentFiles\{file_name}.txt"
    program = get_program("Enter a program (\"All\" for all): ")

    if os.path.exists(file_name):
        os.remove(file_name)

    file = open(file_name, "a")
    file.write("Student list:\r\r")
    file.close()

    for student in students:
        if student.program == program:
            student.output_to_file(file_name)
        elif program == "All":
            student.output_to_file(file_name)
#Creates a file for specific students


def get_menu_option():
    print("\n1. List students")
    print("2. Add a student")
    print("3. Remove a student")
    print("4. Create file from students")
    print("5. Exit")
    return int(input("\n\tSelection: "))
#Prints out all possible menu options
    

def list_students():
    i = 1
    print("\n")
    for student in students:
        print(f"{i}. {student.__str__()}")
        i += 1
#Lists all students in order of the list

def remove_student():
    list_students()
    student_to_remove = int(input("\n\tWhich student would you like to remove: ")) - 1
    students.pop(student_to_remove)
#Removes specific student from list of students
    
while True:
    option = get_menu_option()
    if option == 1:
        list_students()
    elif option == 2:
        add_student()
    elif option == 3:
        remove_student()
    elif option == 4:
        create_file()
    elif option == 5:
        break
    else:
        print("Enter valid option.")
#Asks for a menu option and then runs the appropriate function

print("Thank you for teaching me python!")
print("I appreciate it and believe I will actually use this in the future:)")
#Conclusion statement

