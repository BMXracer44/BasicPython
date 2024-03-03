import re 

# ====Data Validation====

###Validate an int based on a prompt
def get_int(prompt):
    while True:
        try: 
            user_num = input(prompt)
            return int(user_num)
        except:
            print("Please enter a number")
            ##continue restarts a loop
            continue



#Get int inside of a range using bottom and top and get extra credit
#Add function get int in range

def get_int_in_range(prompt, bottom, top):
    user_input = int(input(prompt))
    if(user_input >= bottom and user_input <= top):
        return user_input
    else:
        print("Please enter a number in range")
        return get_int_in_range(prompt, bottom, top)

#Validate email using Regex
def get_valid_email(prompt):
    #This pattern is from https://uibakery.io/regex-library/email-regex-python
    email_pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 

    while True:
        email = input(prompt)
        is_match = re.match(email_pattern, email)
        if is_match:
            return email
        else:
            print("Enter a valid email.")

#Validate only letters
def get_only_letters(prompt):
    letters_pattern = "^[a-zA-Z]*$"
    
    while True:
        user_input = input(prompt)
        is_match = re.match(letters_pattern, user_input)
        if is_match:
            return user_input
        else:
            print("Enter only letters. ")

def get_username(prompt):
    letters_pattern = "^[a-zA-Z]{6}[0-9]{2}$"
    
    while True:
        user_input = input(prompt)
        is_match = re.match(letters_pattern, user_input)
        if is_match:
            return user_input
        else:
            print("Enter 6 letters and 2 numbers. ")

programs = [
    "Web and Software",
    "Cybersecurity",
    "Network Specialist"
]
def get_program(prompt):
    while True:
        user_input = input(prompt)
        for program in programs:
            if(user_input == program):
                return user_input
            if(user_input == "All"):
                return user_input
        print("Enter a valid program. ")

        