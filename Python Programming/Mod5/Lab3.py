#Alex Ferguson
#Mod 5 Lab 3
#Python
#5/2/2023

from helper import *
import re

# Regular Expression basics (regex)
# ^ start a pattern
# $ end a pattern
# [] to determine characters
#       i.e. [a-z] lowercase    [A-Z] uppercase   [a-zA-Z] both
# {} to determine
#       i.e. {2,5} is 2-5   {5,} at least 5


#At least 5 characters of lower and uppercase letters (no numbers)
user_input = input("Enter 5 or more letters: ")
pattern_one = "^[a-zA-Z]{5,}$"

is_match = re.search(pattern_one, user_input)

if is_match:
    print(f"{user_input} is valid")
else:
    print("Try following directions")

#For a username that had 6 lowercase letters followed by 2 numbers
user_input = input("6 letters, 2 numbers: ")
pattern_two = "^[a-z]{6}[0-9]{2}$"

is_match = re.search(pattern_two, user_input)

if is_match:
    print(f"{user_input} is valid")
else:
    print("Try following directions")

#Validate emails using our helper file
email = get_valid_email("Please enter an email: ")

print(f"{email} has been added to the spam list")