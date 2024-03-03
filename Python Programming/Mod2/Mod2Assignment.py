#Alex Ferguson
#Python
#Mod 2 Assignment
#Due 04/12/2023

print("=== Budget Calculator ===\n")

def get_cost(expense):
    payment = input(f"\nDo you pay for {expense}? (y/n): ")
    if payment == 'y':
        return (float(input(f"    How much is {expense} per month: $")))
    else:
        return 0
#Function to get the cost of a special expense

pay_period = int(input("Enter how many times are you paid per month: "))
#Asks how many times you get paid per month and stores that value in a variable

paycheck = float(input("Enter how much each paycheck is post-tax: $"))
#Asks how much you get paid per paycheck and stores that value in a variable

monthly_income = pay_period * paycheck
#Calculates your monthly income based off of information the user has given

rent_payment = get_cost("rent")
#Gets the cost of rent payments

grocery_payment = get_cost("groceries")
#Gets the cost of grocery payments

car_payment = get_cost("a car")
#Gets the cost of car payments

total_expenses = rent_payment + grocery_payment + car_payment
#Calculates the users total expense based off of information the user has already given

def print_report(income, cost):
    print(f"\nMonthly income: ${income}")
    print(F"Monthly expenses: ${cost}")
    #Prints the users monthly income and monthly expenses

    total = income - cost
    #Calculates the users surplus or deficit
    if total > 0:
        print(f"\nYou are running a surplus of ${total}")
    elif total == 0:
        print("\nYou are breaking even!")
    else:
        print(f"\nYou are running a deficit of ${abs(total)}")
    #Tells the user if they have a surplus or a deficit

print_report(monthly_income, total_expenses)
#Prints the report