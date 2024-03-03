#Alex Ferguson
#Python
#Mod 2 Lab 2
#Due: 04/12/2023


def calc_change(amount_of_money):
    if amount_of_money > .99:
        print(f"You have {int(amount_of_money // 1)} dollars")
        amount_of_money = round(amount_of_money % 1, 2)
        #Prints the amount of dollars and then changes the amount of money

    if amount_of_money >= .25:
        print(f"You have {int(amount_of_money // .25)} quarters")
        amount_of_money = round(amount_of_money % .25, 2)
        #Prints the amount of quarters and then changes the value

    if amount_of_money >= .1:
        print(f"You have {int(amount_of_money // .1)} dimes")
        amount_of_money = round(amount_of_money % .1, 2)
        #Prints the amount of dimes and then changes the value

    if amount_of_money >= .05:
        print(f"You have {int(amount_of_money // .05)} nickles")
        amount_of_money = round(amount_of_money % .05, 2)
        #Prints the amount of nickles and then changes the value

    if amount_of_money >= .01:
        print(f"You have {int(amount_of_money // .01)} pennies")
        #Prints the amount of pennies

calc_change(round(float(input("Enter how much money you have: ")), 2))

