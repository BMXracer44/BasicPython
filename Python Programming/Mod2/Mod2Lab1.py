#Function header consists of: def   a function name and any parameters
# def print_hi(message):
#   print(message)
#   print("Your message is " + message)

# print_hi("Happy spring!")
# print_hi(Have a great day!)

def area_calculator(width, height):
    return width * height
#Function to complete the area of the desired inputs and return that value

def calc_area_from_user():
    height = float(input("Input a height: "))
    width = float(input("Input a width: "))
    print(f"The area is {area_calculator(height, width)} units!")
#Asks for the height and width and outputs the value returned from area_calculator to the console

calc_area_from_user()
calc_area_from_user()
calc_area_from_user()

        
