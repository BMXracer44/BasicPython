#Alex Ferguson
#Python
#Module 1 Lab 3
#Due: 04/05/2023

# #==========Percentage Calculator==========
# initial_value = float(input("Initial value: "))
# percentage = float(input("What percentage: %"))
# #Records the initial value and a percentage 

# percentage_value = initial_value * (percentage / 100)
# #Multiplies the initial value by the percentage stored as a decimal

# print(f"{percentage_value} is %{percentage} of {initial_value}")
####To comment out, highlight and then control "/" (?)


initial_value = float(input("Initial amount: $"))
interest_rate = float(input("What interest: %"))
#Records the initial value and an APR

interest_rate = interest_rate / 100

compound_per_period = 12.0

years = float(input("How many years: "))

accrued_amount = initial_value * (1 + interest_rate / compound_per_period)**(compound_per_period*years)
print(f"Total amount: ${accrued_amount:,.2f}")