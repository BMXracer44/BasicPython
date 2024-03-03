#Alex Ferguson
#Python
#Mod 6 Lab 1
#05/08/2023

file = open("Lab1Files\hello-world.txt", "r")
#Opens text file and stores information in a variable named file

print(file.read())
#Prints everything in the text file that was given to the variable 'file'

print(file.tell())
#Prints out where the code is currently at in the text file (prints character number)

file.seek(0)

i = 1
for line in file:
    line = line.rstrip('\r\n')

    print(f"Line {i}: {line}")
    i += 1

file.close()