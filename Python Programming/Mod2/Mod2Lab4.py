#Alex Ferguson
#Python
#Mod 2 Lab 4
#Due 04/12/2023

from datetime import date

#Make a function that returns a date object
def getbirthdate():
    year = int(input("Enter your birth year: "))
    month = int(input("Enter what month you were born (as a number): "))
    day = int(input("Enter the day you were born: "))
    
    return date(year, month, day)

def get_age(birthdate):
    today = date.today()
    #Delta time is the difference between times
    age = today - birthdate

    return int((age.days + 1) // 365.25)

user_bday = getbirthdate()
user_age = get_age(user_bday)

print(f"You are {user_age} years old!")

if user_age >= 16:
    print("You can drive!")

if user_age >= 18:
    print("You can vote!")

if user_age >= 35:
    nbc = input("Are you a natural born citizen? (y/n): ")
    if nbc == 'y':
        resident = input("Have you been a U.S. resident for 14 years? (y/n): ")
        if resident == 'y':
            print("You can be president!")

if user_age < 35 or user_age > 55:
    print("You are not middle aged!")