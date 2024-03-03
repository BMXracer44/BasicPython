#Alex Ferguson
#Python
#Mod 6 Lab 2
#05/09/2023

beeMovie = open("Lab2Files\Scripts\BeeMovie.txt", "r")

# is_barry = False

# for line in beeMovie:
#     line = line.rstrip("\r\n")
    
#     if is_barry and line != "":
#         print(line)

#     if "Barry:" in line:
#         is_barry = True
#     elif line == "":
#         is_barry = False

def print_lines_by_character(character_name, file_path):

    file = open(file_path, "r")

    is_character = False

    print(f"Lines from {character_name}: ")

    for line in file:
        line = line.rstrip("\r\n")

        if is_character and line != "":
            print(f"\t{line}")

        if character_name + ":" in line:
            is_character = True
        elif line == "":
            is_character = False

    file.close()

print_lines_by_character(input("Bee movie character: "), "Lab2Files\Scripts\Beemovie.txt")
print_lines_by_character(input("Shrek character: "), "Lab2Files\Scripts\Shrek.txt")