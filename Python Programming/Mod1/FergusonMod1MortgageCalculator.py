#Alex Ferguson
#Python
#Mortgage Calculator
#Due: 04/05/2023

print("---=== Mortgage Calculator ===---\n")

principle = float(input("Please enter the total amount of the loan: $"))
#How much you buy the house for

interest_rate = float(input("Please enter the interest rate: %"))
#The APR for the loan

interest_rate = interest_rate / 12.0 / 100
#Calculates the monthly interest rate

years = float(input("Please enter the length of the loan in years: "))
#Asks for the years you will pay the loan for

number_of_payments = 12.0 * years
#How many times the loan compounds per year (Monthly)

monthly_payment = principle * ( ( interest_rate * (1 + interest_rate) ** number_of_payments) / ((1 + interest_rate) ** number_of_payments - 1) )
print(f"\nTotal amount: ${monthly_payment:,.2f}")
#Calculates the total mortgage payment and outputs the amount to the user