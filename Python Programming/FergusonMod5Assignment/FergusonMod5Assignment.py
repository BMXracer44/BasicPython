#Alex Ferguson
#Python
#5/2/2023
#Mod 5 Assignment

from helper import *

print("Welcome to the Employee Management System!")
#Introduction statement

job_descrip = {
    #Sources from https://resources.workable.com/account-manager-job-description#:~:text=An%20Account%20Manager%20is%20in,parties%20for%20future%20business%20ventures.
    "Account Manager": "Make sure each department meets the needs of their clients and customers",
    #sourced from https://www.simplilearn.com/project-manager-job-description-article#:~:text=A%20project%20manager%20is%20accountable,goals%20and%20achieving%20their%20vision.
    "Project Manager": "Planning and allocating resources, preparing budgets, monitoring progress, and keeping stakeholders informed throughout the project lifecycle",
    #Sourced from https://cogsagency.com/looking-for-work/senior-developer-job-description/#:~:text=A%20senior%20developer%20thinks%20strategically,for%20apps%20and%20the%20web.&text=A%20senior%20developer%20may%20manage,efficiency%20throughout%20complex%20digital%20projects.
    "Senior Developer": "Thinking strategically and has a deep understanding of all stages of digital development for apps and the web",
    #Sourced from https://www.betterteam.com/junior-software-developer-job-description
    "Junior Developer": "Assisting the development team with all aspects of software design and coding"
}
#Dictionary of jobs and their descriptions


class Employee:
    def __init__(self, firstname, lastname, username, email, job_title):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.job_title = job_title

    def __str__(self):
        return f"{self.job_title} | {self.firstname}, {self.lastname} | {self.email} | {self.username} \n\t{self.get_job_description()}"
    
    def get_job_description(self):
        if self.job_title in job_descrip:
            return job_descrip[self.job_title]
        else:
            return "No description"
#Class of employees to define, print, and get a description
        

employees = [
    Employee("Alex", "Ferguson", "fergus1234", "fergusalex444@gmail.com", "Account Manager"),
    Employee("Bob", "Ross", "ross1234", "painting@gmail.com", "Project Manager"),
    Employee("Charlie", "Brown", "charlie1234", "charlie@gmail.com", "Junior Developer")
]
#List of employees

def get_menu_option():
    print("\n1. List Employees")
    print("2. Add an Employee")
    print("3. Remove an Employee")
    print("4. Add a job")
    print("5. Exit")
    return get_int("\tSelection: ")
#Function to get a menu


def list_employees():
    i = 1
    for e in employees:
        print(f"{i}. {e}")
        i += 1
#Function to list employees

def list_jobs():
    for r, d in job_descrip.items():
        print(f"{r}:\n\t{d}")
#Function to list jobs

def add_employee():
    firstname = get_only_letters("Firstname: ")
    lastname = get_only_letters("Lastname: ")
    email = get_valid_email("Email: ")
    username = get_valid_username("Username: ")
    role = input("Job title: ")
    new_employee = Employee(firstname, lastname, username, email, role)
    employees.append(new_employee)
#Function to add an employee

def remove_employee():
    list_employees()
    user_index = int(input("\tWhich employee would you like to remove: ")) - 1
    employees.pop(user_index)
#Function to remove an employee

while True:
    option = get_menu_option()
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        remove_employee()
    elif option == 4:
        list_jobs()
    elif option == 5:
        break
    else:
        print("Enter valid option.")
#Asks for a menu option and then runs the appropriate function

print("Thank you for using the Employee Management System!")
#Conclusion statement