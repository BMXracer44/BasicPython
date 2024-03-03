#Alex Ferguson
#Python
#Mod 3 Lab 3
#04/18/23

def loop_letter(word):
    for letter in word:
        print(letter)

loop_letter("Hello world!")
loop_letter("AHHHHHHHHHHH")
loop_letter("iuedrfhgfjihfjkhd")

def loop_numbers(start, end):
    for n in range(start, end):
        print(n)

loop_numbers(int (input("Pick the start number: ")), int( input("Pick the end number: ")) + 1)

def loop_list(list):
    for item in list:
        print(item)
        
my_list = ["Alex", "Chicken wings", 18, False, "Legs"]

loop_list(my_list)