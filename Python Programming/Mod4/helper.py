

# ====Data Validation====

###Validate an int based on a prompt
def get_int(prompt):
    while True:
        try: 
            user_num = input(prompt)
            return int(user_num)
        except:
            print("Please enter a number in range")
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


