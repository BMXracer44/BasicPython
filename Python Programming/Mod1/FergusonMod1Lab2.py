#Alex Ferguson
#Python
#Module 1 Lab 2
#Due: 04/05/2023

print("=========== Mod 1 Lab 2 ===========\n")
#Introduction

a = int(input('Please enter a value for A: '))
b = int(input('Please input a value for B: '))
#Asks and assigns a value for the variables a and b
#Can also make a and b an int if they are wraped in the integer function

#print(a + b)

a_int = int(a)
b_int = int(b)
#Declares a and b as different int variables

#print(a_int + b_int)
#print(int(a) + int(b))
#Two seperate ways to convert to int in a print statement

a = int(a)
b = int(b)
#print(a + b)
#Permanently declares A and B to an int

#print("A is " + a + " and B is " + b)
#Won't work because they are int's

#print("A is " + str(a) + " and B is " + str(b))

print(f"A is {a} and B is {b}")
#Looks for the curly braces and converts whatever is inside to a string

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotent: {a / b}")
print(f"Floor quotent: {a // b}")
print(f"Remainder: {a % b}")
print(f"Power: {a ** b}")
print()
print(f"(a)b-a = {a * b - a}")
print(f"a(b-a) = {a * (b - a)}")
print(f"(a+b)^2 = {(a + b)**2}")
print(f"(a+b)(a^2) = {(a+b)*(a**2)}")
print(f"(a+b^2) / (a-b) = {(a + ( b ** 2)) / (a - b)}")



print("\n=============== End ===============")
#Conclusion